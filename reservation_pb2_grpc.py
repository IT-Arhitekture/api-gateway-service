# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import reservation_pb2 as reservation__pb2


class ReservationGrpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getReservations = channel.unary_unary(
                '/ReservationGrpc/getReservations',
                request_serializer=reservation__pb2.EmptyRequest.SerializeToString,
                response_deserializer=reservation__pb2.ReservationList.FromString,
                )
        self.getReservationByRestaurantId = channel.unary_unary(
                '/ReservationGrpc/getReservationByRestaurantId',
                request_serializer=reservation__pb2.RestaurantIdRequest.SerializeToString,
                response_deserializer=reservation__pb2.ReservationList.FromString,
                )
        self.getReservationByCustomerId = channel.unary_unary(
                '/ReservationGrpc/getReservationByCustomerId',
                request_serializer=reservation__pb2.CustomerIdRequest.SerializeToString,
                response_deserializer=reservation__pb2.ReservationList.FromString,
                )
        self.createReservation = channel.unary_unary(
                '/ReservationGrpc/createReservation',
                request_serializer=reservation__pb2.CreateReservationRequest.SerializeToString,
                response_deserializer=reservation__pb2.Reservation.FromString,
                )
        self.updateReservation = channel.unary_unary(
                '/ReservationGrpc/updateReservation',
                request_serializer=reservation__pb2.UpdateReservationRequest.SerializeToString,
                response_deserializer=reservation__pb2.Reservation.FromString,
                )
        self.deleteReservation = channel.unary_unary(
                '/ReservationGrpc/deleteReservation',
                request_serializer=reservation__pb2.DeleteReservationRequest.SerializeToString,
                response_deserializer=reservation__pb2.EmptyResponse.FromString,
                )


class ReservationGrpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getReservations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getReservationByRestaurantId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getReservationByCustomerId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createReservation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateReservation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteReservation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReservationGrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getReservations': grpc.unary_unary_rpc_method_handler(
                    servicer.getReservations,
                    request_deserializer=reservation__pb2.EmptyRequest.FromString,
                    response_serializer=reservation__pb2.ReservationList.SerializeToString,
            ),
            'getReservationByRestaurantId': grpc.unary_unary_rpc_method_handler(
                    servicer.getReservationByRestaurantId,
                    request_deserializer=reservation__pb2.RestaurantIdRequest.FromString,
                    response_serializer=reservation__pb2.ReservationList.SerializeToString,
            ),
            'getReservationByCustomerId': grpc.unary_unary_rpc_method_handler(
                    servicer.getReservationByCustomerId,
                    request_deserializer=reservation__pb2.CustomerIdRequest.FromString,
                    response_serializer=reservation__pb2.ReservationList.SerializeToString,
            ),
            'createReservation': grpc.unary_unary_rpc_method_handler(
                    servicer.createReservation,
                    request_deserializer=reservation__pb2.CreateReservationRequest.FromString,
                    response_serializer=reservation__pb2.Reservation.SerializeToString,
            ),
            'updateReservation': grpc.unary_unary_rpc_method_handler(
                    servicer.updateReservation,
                    request_deserializer=reservation__pb2.UpdateReservationRequest.FromString,
                    response_serializer=reservation__pb2.Reservation.SerializeToString,
            ),
            'deleteReservation': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteReservation,
                    request_deserializer=reservation__pb2.DeleteReservationRequest.FromString,
                    response_serializer=reservation__pb2.EmptyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ReservationGrpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReservationGrpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getReservations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReservationGrpc/getReservations',
            reservation__pb2.EmptyRequest.SerializeToString,
            reservation__pb2.ReservationList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getReservationByRestaurantId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReservationGrpc/getReservationByRestaurantId',
            reservation__pb2.RestaurantIdRequest.SerializeToString,
            reservation__pb2.ReservationList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getReservationByCustomerId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReservationGrpc/getReservationByCustomerId',
            reservation__pb2.CustomerIdRequest.SerializeToString,
            reservation__pb2.ReservationList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createReservation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReservationGrpc/createReservation',
            reservation__pb2.CreateReservationRequest.SerializeToString,
            reservation__pb2.Reservation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateReservation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReservationGrpc/updateReservation',
            reservation__pb2.UpdateReservationRequest.SerializeToString,
            reservation__pb2.Reservation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteReservation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReservationGrpc/deleteReservation',
            reservation__pb2.DeleteReservationRequest.SerializeToString,
            reservation__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
