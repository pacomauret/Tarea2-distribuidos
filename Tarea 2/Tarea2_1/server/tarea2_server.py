from concurrent import futures
import logging

import grpc
import sys
import tarea2_pb2
import tarea2_pb2_grpc
import time

class Tarea2(tarea2_pb2_grpc.TareaRPCServicer):
	def __init__(self):
		self.lastPrintTime =time.time()
		self.usuarios=[]
		self.mensajes=[]
		self.len_mensajes=0
		self.Queue_mensajes=dict()
		self.All_messages=dict()



	def actualizar_usuarios(self,request,context):
		self.usuarios.append(str(request.name))
		if (request.name not in self.Queue_mensajes):
			self.Queue_mensajes[str(request.name)]=[]
		#	print("que wea con el nombre!!=",str(request.name))
		#	print("self.Queue_mensajes=",self.Queue_mensajes)
		#print("la lista de usuarios tiene:",self.usuarios)

		return tarea2_pb2.Confirmation(message="ok")

	def Read_Message(self,request,context):
		inbox=""
		if (request.name not in self.Queue_mensajes):
			p=3
		else:
			inbox_unprepared=self.Queue_mensajes[request.name]
			for i in inbox_unprepared:
				inbox=i+"|"
			self.Queue_mensajes[request.name]=[]
#		print ("inbox=|",inbox,"|")
		return tarea2_pb2.Inbox(mensaje=inbox)


	def Send_Message(self,request,context):
		time_stamp = time.ctime(time.time())
		#print("nombre="+request.name+" mensaje= "+request.mensaje+ " destino= "+request.destino)
	

		nota="DE: "+str(request.name)+" PARA: "+str(request.destino)+ "; CON EL MENSAJE: "+str(request.mensaje).strip()+";ID_Mensaje: "+str(self.len_mensajes)+'--'+str(time_stamp)
		print(nota)
		myfile=open("log.txt",'a')
		myfile.write(nota)
		myfile.close()
		self.len_mensajes+=1
		nota_buzon="DE: "+str(request.name)+" CON EL MENSAJE: "+request.mensaje+'--'+ str(time_stamp)
		if (request.destino not in self.Queue_mensajes):
			self.Queue_mensajes[str(request.destino)]=[]
		self.Queue_mensajes[str(request.destino)].append(str(nota_buzon))
		#print("LA QUEUE TIENE: ",self.Queue_mensajes)
		if (str(request.name) not in self.All_messages):
			self.All_messages[str(request.name)]=[]
		self.All_messages[str(request.name)].append("Destino: "+str(request.destino)+", con el texto: "+str(request.mensaje)+'--'+ str(time_stamp))
		return tarea2_pb2.Confirmation(message="ok")

	def See_users(self,request,context):
		users=""
		for i in self.usuarios:
			users+=";"+i
		return tarea2_pb2.Inbox(mensaje=users)

	def See_messages(self,request,context):
		user=str(request.name).strip()
		todos=""
		count=0
		try:
			largo=len(self.All_messages[user])
		except:
			largo=0
		if (largo!=0):
			for i in self.All_messages[user]:
				todos+=i.strip()
				if ((largo-count)>1):
					todos+="|"
		else:
			todos=''
		return tarea2_pb2.Inbox(mensaje=todos)






def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	tarea2_pb2_grpc.add_TareaRPCServicer_to_server(Tarea2(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	print("Server started [x]")
	server.wait_for_termination()
	self.myfile.close()

if __name__ == '__main__':
#    logging.basicConfig()
    serve()
