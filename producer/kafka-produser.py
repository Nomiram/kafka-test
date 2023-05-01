'''Kafka Producer'''

import json
import random
import time
from json import dumps

from kafka import KafkaProducer

MAX_RETRY = 5
producer = KafkaProducer(bootstrap_servers=['kafka_0:9092', 'kafka_1:9093', 'kafka_2:9094',],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

i = 0
for i in range(10):
    i += 1
    message = random.choice([{"type": "message"}, {"type": "error"}])

    print(message)
    ack = producer.send("main_topic", message)
    metadata = ack.get()
    print(
        f"Send to topic: '{metadata.topic}' partition: {metadata.partition} offset: {metadata.offset}")
producer.flush()
producer.close()
