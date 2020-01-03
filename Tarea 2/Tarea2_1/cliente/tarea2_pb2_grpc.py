# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import tarea2_pb2 as tarea2__pb2


class TareaRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Read_Message = channel.unary_unary(
        '/tareaRPC.TareaRPC/Read_Message',
        request_serializer=tarea2__pb2.Usuario.SerializeToString,
        response_deserializer=tarea2__pb2.Inbox.FromString,
        )
    self.actualizar_usuarios = channel.unary_unary(
        '/tareaRPC.TareaRPC/actualizar_usuarios',
        request_serializer=tarea2__pb2.Usuario.SerializeToString,
        response_deserializer=tarea2__pb2.Confirmation.FromString,
        )
    self.Send_Message = channel.unary_unary(
        '/tareaRPC.TareaRPC/Send_Message',
        request_serializer=tarea2__pb2.Destined_Message.SerializeToString,
        response_deserializer=tarea2__pb2.Confirmation.FromString,
        )
    self.See_users = channel.unary_unary(
        '/tareaRPC.TareaRPC/See_users',
        request_serializer=tarea2__pb2.Usuario.SerializeToString,
        response_deserializer=tarea2__pb2.Inbox.FromString,
        )
    self.See_messages = channel.unary_unary(
        '/tareaRPC.TareaRPC/See_messages',
        request_serializer=tarea2__pb2.Usuario.SerializeToString,
        response_deserializer=tarea2__pb2.Inbox.FromString,
        )


class TareaRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Read_Message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def actualizar_usuarios(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Send_Message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def See_users(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def See_messages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TareaRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Read_Message': grpc.unary_unary_rpc_method_handler(
          servicer.Read_Message,
          request_deserializer=tarea2__pb2.Usuario.FromString,
          response_serializer=tarea2__pb2.Inbox.SerializeToString,
      ),
      'actualizar_usuarios': grpc.unary_unary_rpc_method_handler(
          servicer.actualizar_usuarios,
          request_deserializer=tarea2__pb2.Usuario.FromString,
          response_serializer=tarea2__pb2.Confirmation.SerializeToString,
      ),
      'Send_Message': grpc.unary_unary_rpc_method_handler(
          servicer.Send_Message,
          request_deserializer=tarea2__pb2.Destined_Message.FromString,
          response_serializer=tarea2__pb2.Confirmation.SerializeToString,
      ),
      'See_users': grpc.unary_unary_rpc_method_handler(
          servicer.See_users,
          request_deserializer=tarea2__pb2.Usuario.FromString,
          response_serializer=tarea2__pb2.Inbox.SerializeToString,
      ),
      'See_messages': grpc.unary_unary_rpc_method_handler(
          servicer.See_messages,
          request_deserializer=tarea2__pb2.Usuario.FromString,
          response_serializer=tarea2__pb2.Inbox.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tareaRPC.TareaRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
