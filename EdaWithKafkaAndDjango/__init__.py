from __future__ import absolute_import, unicode_literals

from order.celery import app as celery_app
from order.tasks import process_order

__all__ = ["celery_app", "process_order"]
