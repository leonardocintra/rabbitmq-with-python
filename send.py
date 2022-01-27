#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('senhadigital', 'senhadigital')
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials, virtual_host='senhadigital-rabbitmq')
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()