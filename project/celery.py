import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Configure Celery Beat to schedule the task
app.conf.beat_schedule = {
    'reduce-every-3-seconds': {
        'task': 'BorderPay.tasks.print_hey',
        'schedule': 10.0,  # Run every 3 seconds
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')