from django.http import JsonResponse

from order.kafka_producer import kafka_produce
from order.models import Order


def order_list(request):
    order: Order = Order.objects.create(customer_name="Onur")
    message = f"Order created: {order.id} for customer: {order.customer_name}"
    kafka_produce(topic="order-events", message=message)
    return JsonResponse({"message": "Order created successfully and sent to kafka."})


def run_consumer(request):
    from consumer.tasks import consume_kafka_messages

    consume_kafka_messages.delay()
    return JsonResponse({"message": "Kafka consumer started."})
