import os
import logging
from threading import Thread
from fastapi import FastAPI, BackgroundTasks
from worker.celery_app import celery_app

# Issue a warning regarding a particular runtime event
log = logging.getLogger(__name__)

app = FastAPI()

def celery_on_message(body):
    log.warn(body)

def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propagate=False))

# creating an API endpoint that accepts an item_id, creates a tasks_id, puts the tasks_id and item_id in the Celery queue, and return task, 
returns the task_id
@app.get("/{item_id}")
async def root(item_id: str, background_task: BackgroundTasks):
    task_name = None
    task_name = "app.app.worker.celery_worker.test_celery"

# Send task to celery worker
    task = celery_app.send_task(task_name, args=[item_id])
    print(task)
    background_task.add_task(background_on_message, task)

    return {"message": "item_id received"}
