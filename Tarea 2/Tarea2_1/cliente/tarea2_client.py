from __future__ import print_function
import logging
import sys
import grpc
import os
import tarea2_pb2
import tarea2_pb2_grpc
from threading import Thread


class ClientThread(Thread): 

	def __init__(self,name):
		Thread.__init__(self)
		self.name=name


	def run(self):

  		mensaje_sintratar=input("Inserte mensaje: ")
  		mensaje=mensaje_sintratar.split(";")
  		return mensaje


from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)
"""
def run2():
	mensaje_sintratar=input("Inserte mensaje: ")
	mensaje=mensaje_sintratar.split(";")
	return mensaje
"""

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
	channel = grpc.insecure_channel('server:50051')
	stub = tarea2_pb2_grpc.TareaRPCStub(channel)
	usuario=(str(os.getpid())).strip()
	send=ClientThread(str(usuario))
	stub.actualizar_usuarios(tarea2_pb2.Usuario(name=str(usuario)))
	print("Nombre de usuario =",usuario)
	counter=0
	try:
		while True:
			Inbox_future = stub.Read_Message.future(tarea2_pb2.Usuario(name=str(usuario)))
			Inbox = Inbox_future.result()
			if (Inbox!=''):
				print ("inbox=",Inbox)
			sys.stdout.write("Mensaje o accion:")
			sys.stdout.flush()
			mensaje = sys.stdin.readline()
			if (mensaje[0]=="!"):
				if (mensaje[1:].strip()=="usuarios"):
					response_future = stub.See_users.future(tarea2_pb2.Usuario(name=str(usuario)))
					response = response_future.result()
					print(response)
				if (mensaje[1:].strip()=="mensajes"):
					response_future = stub.See_messages.future(tarea2_pb2.Usuario(name=str(usuario)))
					response = response_future.result()
					res=(str(response).strip()).split(";")
					print(response)
			else:
				mensaje =mensaje.split(";")
				response_future = stub.Send_Message.future(tarea2_pb2.Destined_Message(name=usuario,destino=mensaje[0],mensaje=mensaje[1]))
				response = response_future.result()
	except KeyboardInterrupt:
		print("KeyboardInterrupt")
		channel.unsuscribe(close)
		exit()

def close():
	channel.close()

if __name__ == '__main__':
    logging.basicConfig()
    run()



