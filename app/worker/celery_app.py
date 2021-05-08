import os
from celery import Celery

celery_app = None

celery_app = Celery(
    "worker",
    backend="redis://:password123@redis:6379/0",
    broker="amqp://user:bitnami@rabbitmq:5672//"
    )
celery_app.conf.task_routes = {
    "app.app.worker.celery_worker.test_celery": "test-queue"}

celery_app.conf.update(task_track_started=True)
