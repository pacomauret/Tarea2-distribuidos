import pika
import sys
connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='localhost'))


channel = connection.channel()
channel.exchange_declare(exchange='chats', exchange_type='fanout')

result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='chats', queue=queue_name)
a=dict()
def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)
	mes=(str(body).strip()).split(";")
	print("and the mes its= ",mes,"with queue name = ",result.method.queue)

#	sys.stdout.write("Dame un numero:")
#	sys.stdout.flush()
#	message = sys.stdin.readline()
#	channel.basic_publish(exchange="", routing_key='server', body=message)

channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

print("que_wea_con_la_vida")