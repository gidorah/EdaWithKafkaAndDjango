from celery import shared_task
from confluent_kafka import Consumer, KafkaError, KafkaException


@shared_task
def consume_kafka_messages():
    conf = {
        "bootstrap.servers": "kafka:9092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(conf)

    def print_assignment(consumer, partitions):
        print("Assignment:", partitions)

    consumer.subscribe(["order-events"], on_assign=print_assignment)

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(
                        "%% %s [%d] reached end at offset %d\n"
                        % (msg.topic(), msg.partition(), msg.offset())
                    )
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(
                    "%% %s [%d] at offset %d with key %s:\n"
                    % (msg.topic(), msg.partition(), msg.offset(), str(msg.key()))
                )
                print(msg.value())
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
