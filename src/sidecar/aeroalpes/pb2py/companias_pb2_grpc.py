# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import companias_pb2 as companias__pb2


class CompaniasStub(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CrearCompania = channel.unary_unary(
                '/companias.Companias/CrearCompania',
                request_serializer=companias__pb2.Compania.SerializeToString,
                response_deserializer=companias__pb2.RespuestaCompania.FromString,
                )


class CompaniasServicer(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def CrearCompania(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompaniasServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CrearCompania': grpc.unary_unary_rpc_method_handler(
                    servicer.CrearCompania,
                    request_deserializer=companias__pb2.Compania.FromString,
                    response_serializer=companias__pb2.RespuestaCompania.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'companias.Companias', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Companias(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    @staticmethod
    def CrearCompania(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/companias.Companias/CrearCompania',
            companias__pb2.Compania.SerializeToString,
            companias__pb2.RespuestaCompania.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
