'''Kafka Producer'''
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

i = 0
for i in range(10):
    i+=1
    message = "message"+str(i)
    print(message)
    ack = producer.send("topic_name", message)
    metadata = ack.get()
    print(f"Topic: '{metadata.topic}' partition: {metadata.partition} offset: {metadata.offset}")
