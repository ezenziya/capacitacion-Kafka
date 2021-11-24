from kafka import KafkaConsumer
consumer = KafkaConsumer('quickstart-events')
for message in consumer:
    print (message)