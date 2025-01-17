import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EdaWithKafkaAndDjango.settings")

app = Celery("EdaWithKafkaAndDjango")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
