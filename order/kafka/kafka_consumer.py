from time import sleep

from confluent_kafka import Consumer, KafkaException

from order.tasks import process_order


def kafka_consume(topic):
    conf = {
        "bootstrap.servers": "kafka:9092",
        "client.id": "django-consumer",
        "group.id": "django-consumer-group",
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(conf)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException:
                    continue
                else:
                    raise KafkaException(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')}")
                # process_order.delay(msg.value().decode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    sleep(10)
    kafka_consume(topic="order-events")
