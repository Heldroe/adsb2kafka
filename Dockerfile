FROM python:3

LABEL org.opencontainers.image.source=https://github.com/Heldroe/adsb2kafka

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY adsb2kafka.py .

ENTRYPOINT ["python", "-m", "adsb2kafka"]
CMD []
