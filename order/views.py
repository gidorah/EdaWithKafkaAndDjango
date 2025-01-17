from django.http import JsonResponse

from order.kafka import kafka_produce
from order.models import Order


def order_list(request):
    order: Order = Order.objects.create(customer_name="Onur")
    message = f"Order created: {order.id} for customer: {order.customer_name}"
    kafka_produce(topic="order-events", message=message)
    return JsonResponse({"message": "Order created successfully and sent to kafka."})
