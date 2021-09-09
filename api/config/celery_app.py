from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("apps")


# The celery settings should be preceded with an UPPERCASE CELERY prefix in the settings file
app.config_from_object("django.conf:settings", namespace="CELERY")

# autodiscover celery tasks
app.autodiscover_tasks()
