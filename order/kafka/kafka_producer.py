from confluent_kafka import Producer


def kafka_produce(topic, message):
    conf = {"bootstrap.servers": "kafka:9092", "client.id": "django-producer"}
    producer = Producer(conf)
    producer.produce(topic, value=message)
    producer.flush()


"""
from order.kafka import kafka_produce
kafka_produce(topic="order-events", message="hello")
"""
