from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)
producer.produce('quickstart-events', key="Hello, World!", value="This is Kafka-Python")
producer.poll(1)
producer.flush()
