Использование:

1. Убедиться, что запущен docker и установлен docker-compose версии 3 и выше
2. Запустить Kafka и Zookeeper: `docker-compose up -d`
3. Установить пакет kafka-python: `pip install kafka-python`
4. Запустить kafka-consumer.py в одной консоли
5. Запустить kafka-producer.py в другой консоли
6. Остановить Kafka и Zookeeper:`docker-compose down`

Для тестирования может использоваться контейнер test:

`docker-compose exec test sh`

Consumer:

`kcat -C -b kafka:29092 -t topic_name`

Producer:

`echo 123 | kcat -P -b kafka:29092 -t topic_name`
