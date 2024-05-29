import time

from celery import shared_task


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    if int(task_type) == 2:
        raise Exception("task failed")
    print(50 * "-")
    print()
    print("task created")
    print(f"task_type: {task_type}")
    print()
    print(50 * "-")
    return True
