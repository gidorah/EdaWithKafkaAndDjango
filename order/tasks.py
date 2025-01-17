from celery import shared_task


@shared_task
def process_order(order_data):
    print(f"Processing order: {order_data}")
    return f"Processed order: {order_data}"
