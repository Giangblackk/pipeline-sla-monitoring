from dagster import asset, Config
import time


class TaskRunTimeConfig(Config):
    runtime_mins: float = 1.0
    secs_per_min: int = 60


@asset
def task_1(config: TaskRunTimeConfig):
    print("start task 1")
    default_runtime_mins = 3
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 1")


@asset(deps=[task_1])
def task_2(config: TaskRunTimeConfig):
    print("start task 2")
    default_runtime_mins = 5.9
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 2")


@asset
def task_4(config: TaskRunTimeConfig):
    print("start task 4")
    default_runtime_mins = 3
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 4")


@asset(deps=[task_1, task_4])
def task_3(config: TaskRunTimeConfig):
    print("start task 3")
    default_runtime_mins = 1.5
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 3")


@asset(deps=[task_3, task_4])
def task_5(config: TaskRunTimeConfig):
    print("start task 5")
    default_runtime_mins = 2
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 5")


@asset(deps=[task_2, task_3])
def task_6(config: TaskRunTimeConfig):
    print("start task 6")
    default_runtime_mins = 0.3
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 6")


@asset(deps=[task_5, task_6, task_3])
def task_7(config: TaskRunTimeConfig):
    print("start task 7")
    default_runtime_mins = 4
    if config.runtime_mins != default_runtime_mins:
        runtime_mins = config.runtime_mins
    else:
        runtime_mins = config.runtime_mins
    time.sleep(runtime_mins * config.secs_per_min)
    print("end task 7")
