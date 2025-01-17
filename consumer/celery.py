from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EdaWithKafkaAndDjango.settings")

app = Celery("EdaWithKafkaAndDjango")

# Load settings from Django settings file
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks in all registered Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
