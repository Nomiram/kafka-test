'''Kafka Consumer'''
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "topic_name",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest')

print("starting the consumer")
for msg in consumer:
    print(msg)
    print(msg.value)
