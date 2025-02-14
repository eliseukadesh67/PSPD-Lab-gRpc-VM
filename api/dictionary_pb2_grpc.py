# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import dictionary_pb2 as dictionary__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in dictionary_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DictionaryServiceStub(object):
    """Serviço gRPC
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddWord = channel.unary_unary(
                '/dictionary.DictionaryService/AddWord',
                request_serializer=dictionary__pb2.WordEntry.SerializeToString,
                response_deserializer=dictionary__pb2.Status.FromString,
                _registered_method=True)
        self.GetWord = channel.unary_unary(
                '/dictionary.DictionaryService/GetWord',
                request_serializer=dictionary__pb2.WordRequest.SerializeToString,
                response_deserializer=dictionary__pb2.WordResponse.FromString,
                _registered_method=True)


class DictionaryServiceServicer(object):
    """Serviço gRPC
    """

    def AddWord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DictionaryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddWord': grpc.unary_unary_rpc_method_handler(
                    servicer.AddWord,
                    request_deserializer=dictionary__pb2.WordEntry.FromString,
                    response_serializer=dictionary__pb2.Status.SerializeToString,
            ),
            'GetWord': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWord,
                    request_deserializer=dictionary__pb2.WordRequest.FromString,
                    response_serializer=dictionary__pb2.WordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dictionary.DictionaryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('dictionary.DictionaryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DictionaryService(object):
    """Serviço gRPC
    """

    @staticmethod
    def AddWord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.DictionaryService/AddWord',
            dictionary__pb2.WordEntry.SerializeToString,
            dictionary__pb2.Status.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetWord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dictionary.DictionaryService/GetWord',
            dictionary__pb2.WordRequest.SerializeToString,
            dictionary__pb2.WordResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
