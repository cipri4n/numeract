from time import sleep
from celery import current_task
from .celery_app import celery_app


# task creation which represents endpoint that returns the status: processing for 10 seconds
@celery_app.task(acks_late=True)
def test_celery(item_id: str) -> str:
    for i in range(1, 10):
        sleep(1)
        current_task.update_state(state='processing',
                                  meta={'process stage: ': i})
    return f"Task returned: {item_id}"
