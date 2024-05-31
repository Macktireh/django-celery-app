from celery import shared_task
from celery.utils.log import get_task_logger
# from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task
def sample_task_1():
    print(80 * "-")
    print("\n")
    print("sample_task_1")
    print("\n")
    logger.info("The sample task just ran.")
    logger.warning("The sample task just ran.")
    logger.error("The sample task just ran.")
    logger.critical("The sample task just ran.")
    logger.debug("The sample task just ran.")
    print()
    print(80 * "-")


@shared_task
def sample_task_2():
    print(80 * "-")
    print("\n")
    print("sample_task_2")
    print("\n")
    logger.info("The sample task just ran.")
    logger.warning("The sample task just ran.")
    logger.error("The sample task just ran.")
    logger.critical("The sample task just ran.")
    logger.debug("The sample task just ran.")
    print()
    print(80 * "-")


@shared_task
def sample_task_3():
    print(80 * "-")
    print("\n")
    print("sample_task_3")
    print("\n")
    logger.info("The sample task just ran.")
    logger.warning("The sample task just ran.")
    logger.error("The sample task just ran.")
    logger.critical("The sample task just ran.")
    logger.debug("The sample task just ran.")
    print()
    print(80 * "-")
