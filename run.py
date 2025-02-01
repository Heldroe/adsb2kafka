#!/usr/bin/env python3

import argparse
import signal
import sys

from confluent_kafka import Producer

import pyModeS as pms
from pyModeS.extra.tcpclient import TcpClient


parser = argparse.ArgumentParser(description="beast2kafka: publish Beast protocol frames into Kafka.")

parser.add_argument(
    '--bootstrap-servers',
    type=str,
    required=True,
    help='Comma-separated list of Kafka bootstrap servers (host:port).',
)
parser.add_argument(
    '--kafka-topic',
    type=str,
    default='adsb.frames',
    help='Kafka topic to publish Beast frames to.',
)
parser.add_argument(
    '--beast-host',
    type=str,
    required=True,
    help='Beast server host.'
)
parser.add_argument(
    '--beast-port',
    type=int,
    default=30005,
    help='Beast server port.',
)

args = parser.parse_args()


class ADSBClient(TcpClient):
    def __init__(self, host, port, rawtype, kafka_producer, kafka_topic):
        self.kafka_producer = kafka_producer
        self.kafka_topic = kafka_topic
        super(ADSBClient, self).__init__(host, port, rawtype)

    def handle_messages(self, messages):
        for msg, timestamp in messages:
            self.kafka_producer.poll(0)

            if len(msg) != 28: # Wrong data length
                continue

            if pms.df(msg) != 17: # Not ADSB
                continue

            if pms.crc(msg) !=0: # CRC failure
                continue

            self.kafka_producer.produce(
                topic=self.kafka_topic,
                value=bytes.fromhex(msg),
                key=bytes.fromhex(pms.adsb.icao(msg)),
                timestamp=round(timestamp * 1000),
            )


kafka_producer = Producer({
    'bootstrap.servers': args.bootstrap_servers,
})
client = ADSBClient(host=args.beast_host, port=args.beast_port, rawtype='beast', kafka_producer=kafka_producer, kafka_topic=args.kafka_topic)


def graceful_shutdown(signum, frame):
    print(f"Received signal {signum}, shutting down gracefully...")
    client.stop()
    kafka_producer.flush()
    sys.exit(0)


signal.signal(signal.SIGINT, graceful_shutdown)  # Handle Ctrl+C
signal.signal(signal.SIGTERM, graceful_shutdown) # Handle termination signal

client.run()
