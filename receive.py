#!/usr/bin/env python
from cmath import pi
import ssl
import pika, sys, os

def main():
    credentials = pika.PlainCredentials('senhadigital', 'senhadigital')
    parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials, virtual_host='senhadigital-rabbitmq')
    connection = pika.BlockingConnection(parameters=parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)