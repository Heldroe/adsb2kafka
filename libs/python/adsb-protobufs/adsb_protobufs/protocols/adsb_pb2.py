# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protocols/adsb.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'protocols/adsb.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protocols/adsb.proto\"2\n\tADSBFrame\x12\x11\n\tsource_id\x18\x01 \x01(\r\x12\x12\n\nframe_data\x18\x02 \x01(\x0c\"\\\n\x10\x41irbornePosition\x12\x11\n\tsource_id\x18\x01 \x01(\r\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x05\"\xda\x01\n\x10\x41irborneVelocity\x12\x11\n\tsource_id\x18\x01 \x01(\r\x12\r\n\x05speed\x18\x02 \x01(\r\x12\x0f\n\x07heading\x18\x03 \x01(\x02\x12\x16\n\x0evertical_speed\x18\x04 \x01(\x11\x12/\n\nspeed_type\x18\x05 \x01(\x0e\x32\x1b.AirborneVelocity.SpeedType\"J\n\tSpeedType\x12\x10\n\x0cGROUND_SPEED\x10\x00\x12\x17\n\x13INDICATED_AIR_SPEED\x10\x01\x12\x12\n\x0eTRUE_AIR_SPEED\x10\x02\"P\n\x16\x41ircraftIdentification\x12\x11\n\tsource_id\x18\x01 \x01(\r\x12\x11\n\tcall_sign\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protocols.adsb_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADSBFRAME']._serialized_start=24
  _globals['_ADSBFRAME']._serialized_end=74
  _globals['_AIRBORNEPOSITION']._serialized_start=76
  _globals['_AIRBORNEPOSITION']._serialized_end=168
  _globals['_AIRBORNEVELOCITY']._serialized_start=171
  _globals['_AIRBORNEVELOCITY']._serialized_end=389
  _globals['_AIRBORNEVELOCITY_SPEEDTYPE']._serialized_start=315
  _globals['_AIRBORNEVELOCITY_SPEEDTYPE']._serialized_end=389
  _globals['_AIRCRAFTIDENTIFICATION']._serialized_start=391
  _globals['_AIRCRAFTIDENTIFICATION']._serialized_end=471
# @@protoc_insertion_point(module_scope)
