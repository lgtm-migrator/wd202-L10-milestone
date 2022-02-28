import os
from datetime import timedelta

from django.conf import settings

from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
app = Celery("tasks")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# Periodic Task
# @periodic_task(run_every=timedelta(seconds=30))
# def every_30_seconds():
#     print("Running Every 30 Seconds!")
