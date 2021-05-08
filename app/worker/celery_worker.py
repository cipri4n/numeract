from time import sleep
from celery import current_task
from .celery_app import celery_app
#from read.read_data import duration_item_id

@celery_app.task(acks_late=True)
def test_celery(item_id: str) -> str:
    #duration = duration_item_id(item_id)
    for i in range(1, 10):
        sleep(1)
        current_task.update_state(state='processing',
                                  meta={'process -> ': i})
    return f"test task return {item_id}"
