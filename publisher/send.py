
#!/usr/bin/env python
import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
	channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
	print(" [x] Sent 'Hello World!'")
	time.sleep(5)

connection.close()
