# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reservation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11reservation.proto\"\x0e\n\x0c\x45mptyRequest\"\x0f\n\rEmptyResponse\"+\n\x13RestaurantIdRequest\x12\x14\n\x0crestaurantId\x18\x01 \x01(\t\"\'\n\x11\x43ustomerIdRequest\x12\x12\n\ncustomerId\x18\x01 \x01(\t\"R\n\x18\x43reateReservationRequest\x12\x14\n\x0crestaurantId\x18\x01 \x01(\t\x12\x12\n\ncustomerId\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\"i\n\x18UpdateReservationRequest\x12\x15\n\rreservationId\x18\x01 \x01(\t\x12\x14\n\x0crestaurantId\x18\x02 \x01(\t\x12\x12\n\ncustomerId\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\"1\n\x18\x44\x65leteReservationRequest\x12\x15\n\rreservationId\x18\x01 \x01(\t\"\\\n\x0bReservation\x12\x15\n\rreservationId\x18\x01 \x01(\t\x12\x14\n\x0crestaurantId\x18\x02 \x01(\t\x12\x12\n\ncustomerId\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\"5\n\x0fReservationList\x12\"\n\x0creservations\x18\x01 \x03(\x0b\x32\x0c.Reservation2\x99\x03\n\x0fReservationGrpc\x12\x34\n\x0fgetReservations\x12\r.EmptyRequest\x1a\x10.ReservationList\"\x00\x12H\n\x1cgetReservationByRestaurantId\x12\x14.RestaurantIdRequest\x1a\x10.ReservationList\"\x00\x12\x44\n\x1agetReservationByCustomerId\x12\x12.CustomerIdRequest\x1a\x10.ReservationList\"\x00\x12>\n\x11\x63reateReservation\x12\x19.CreateReservationRequest\x1a\x0c.Reservation\"\x00\x12>\n\x11updateReservation\x12\x19.UpdateReservationRequest\x1a\x0c.Reservation\"\x00\x12@\n\x11\x64\x65leteReservation\x12\x19.DeleteReservationRequest\x1a\x0e.EmptyResponse\"\x00\x42+\n\x11\x63om.itarhitektureB\x14ReservationGrpcProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reservation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.itarhitektureB\024ReservationGrpcProtoP\001'
  _globals['_EMPTYREQUEST']._serialized_start=21
  _globals['_EMPTYREQUEST']._serialized_end=35
  _globals['_EMPTYRESPONSE']._serialized_start=37
  _globals['_EMPTYRESPONSE']._serialized_end=52
  _globals['_RESTAURANTIDREQUEST']._serialized_start=54
  _globals['_RESTAURANTIDREQUEST']._serialized_end=97
  _globals['_CUSTOMERIDREQUEST']._serialized_start=99
  _globals['_CUSTOMERIDREQUEST']._serialized_end=138
  _globals['_CREATERESERVATIONREQUEST']._serialized_start=140
  _globals['_CREATERESERVATIONREQUEST']._serialized_end=222
  _globals['_UPDATERESERVATIONREQUEST']._serialized_start=224
  _globals['_UPDATERESERVATIONREQUEST']._serialized_end=329
  _globals['_DELETERESERVATIONREQUEST']._serialized_start=331
  _globals['_DELETERESERVATIONREQUEST']._serialized_end=380
  _globals['_RESERVATION']._serialized_start=382
  _globals['_RESERVATION']._serialized_end=474
  _globals['_RESERVATIONLIST']._serialized_start=476
  _globals['_RESERVATIONLIST']._serialized_end=529
  _globals['_RESERVATIONGRPC']._serialized_start=532
  _globals['_RESERVATIONGRPC']._serialized_end=941
# @@protoc_insertion_point(module_scope)
