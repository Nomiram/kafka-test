Использование:

1. Убедиться, что запущен docker и установлен docker-compose версии 3 и выше
2. Запустить Kafka и Zookeeper: `docker-compose up -d`
3. Запустить kafka-consumer.py в одной консоли
4. Запустить kafka-producer.py в другой консоли
5. Остановить Kafka и Zookeeper:`docker-compose down`

Для тестирования может использоваться контейнер test:

`docker-compose exec test shdocker-compose exec test sh`

Consumer:

`kcat -C -b kafka:29092 -t topic_name`

Producer:

`echo 123 | kcat -P -b kafka:29092 -t topic_name`
