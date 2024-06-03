from dagster import asset, Config, get_dagster_logger
import time
import aiohttp
from typing import Optional


class TaskRunTimeConfig(Config):
    runtime_mins: Optional[float]
    secs_per_min: int = 60


JOB_STATUS_URL = "http://localhost:8000/job/status"


async def log_task_status(task_name: str, status: str):
    async with aiohttp.ClientSession() as session:
        await session.post(
            JOB_STATUS_URL, json={"task_name": task_name, "status": status}
        )


def wait_for(default_runtime_mins: float, config: TaskRunTimeConfig):
    if config.runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = default_runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)


@asset
async def task_1(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 1")
    await log_task_status("task_1", "STARTED")

    default_runtime_mins = 3
    wait_for(default_runtime_mins, config)

    await log_task_status("task_1", "SUCCEEDED")
    logger.info("end task 1")


@asset(deps=[task_1])
async def task_2(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 2")
    await log_task_status("task_2", "STARTED")

    default_runtime_mins = 5.9
    wait_for(default_runtime_mins, config)

    await log_task_status("task_2", "SUCCEEDED")
    logger.info("end task 2")


@asset
async def task_4(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 4")
    await log_task_status("task_4", "STARTED")

    default_runtime_mins = 3
    wait_for(default_runtime_mins, config)

    await log_task_status("task_4", "SUCCEEDED")
    logger.info("end task 4")


@asset(deps=[task_1, task_4])
async def task_3(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 3")
    await log_task_status("task_3", "STARTED")

    default_runtime_mins = 1.5
    wait_for(default_runtime_mins, config)

    await log_task_status("task_3", "SUCCEEDED")
    logger.info("end task 3")


@asset(deps=[task_3, task_4])
async def task_5(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 5")
    await log_task_status("task_5", "STARTED")

    default_runtime_mins = 2
    wait_for(default_runtime_mins, config)

    await log_task_status("task_5", "SUCCEEDED")
    logger.info("end task 5")


@asset(deps=[task_2, task_3])
async def task_6(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 6")
    await log_task_status("task_6", "STARTED")

    default_runtime_mins = 0.3
    wait_for(default_runtime_mins, config)

    await log_task_status("task_6", "SUCCEEDED")
    logger.info("end task 6")


@asset(deps=[task_5, task_6, task_3])
async def task_7(config: TaskRunTimeConfig):
    logger = get_dagster_logger()
    logger.info("start task 7")
    await log_task_status("task_7", "STARTED")

    default_runtime_mins = 4
    wait_for(default_runtime_mins, config)

    await log_task_status("task_7", "SUCCEEDED")
    logger.info("end task 7")
