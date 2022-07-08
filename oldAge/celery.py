import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldAge.settings')
app = Celery('pro', backend='redis://127.0.0.1:6379/1', broker='redis://127.0.0.1:6379/0')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
