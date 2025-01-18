from celery import shared_task
from confluent_kafka import Consumer, KafkaError, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic


@shared_task
def consume_kafka_messages():
    conf = {
        "bootstrap.servers": "kafka:9092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }

    topic_name = "order-events"

    create_topic_if_not_exists(topic_name)

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


def create_topic_if_not_exists(topic_name="order_events"):
    admin_client = AdminClient({"bootstrap.servers": "kafka:9092"})

    # Check if the topic exists
    existing_topics = admin_client.list_topics(timeout=10).topics
    if topic_name not in existing_topics:
        print(f"Topic '{topic_name}' does not exist.")
        # Optionally, create the topic
        try:
            admin_client.create_topics(
                new_topics=[
                    NewTopic(topic=topic_name, num_partitions=1, replication_factor=1)
                ]
            )
            print(f"Topic '{topic_name}' created.")
        except Exception as e:
            print(f"Failed to create topic '{topic_name}': {e}")
            return
