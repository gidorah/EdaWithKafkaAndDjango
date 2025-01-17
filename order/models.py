from datetime import datetime

from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"Order: {self.order_id}"
