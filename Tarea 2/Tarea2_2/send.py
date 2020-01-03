import pika
import sys
import os

def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)


usuario=(str(os.getpid())).strip()
#sys.stdout.write("Dame un numero:")
#sys.stdout.flush()
#message = sys.stdin.readline()
#message=message.strip()
#message=message.split(";")

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#channel.queue_declare(queue='server')

channel.exchange_declare(exchange='chats',
                         exchange_type='fanout')

channel.basic_publish(exchange='chats', routing_key='', body=usuario)
##--------------------------------------------------------------
connection2 = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel2 = connection.channel()

#channel2.queue_declare(queue=usuario)

channel2.exchange_declare(exchange='chats',
                         exchange_type='fanout')

#channel2.basic_publish(exchange='chats', routing_key='', body=usuario)


sys.stdout.write("Dame un numero:")
sys.stdout.flush()
message = sys.stdin.readline()
message=message.strip()

while (message!="!close"):

	channel.basic_publish(exchange='chats', routing_key='', body=message)
	print(" [x] Sent ", message)
	
	sys.stdout.write("Dame un numero:")
	sys.stdout.flush()
	message = sys.stdin.readline()
	message=message.strip()

	




connection.close()