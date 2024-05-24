from dagster import asset
import time


@asset
def task_1():
    print("start task 1")
    default_runtime_mins = 3
    time.sleep(default_runtime_mins * 60)
    print("end task 1")


@asset(deps=[task_1])
def task_2():
    print("start task 2")
    default_runtime_mins = 5.9
    time.sleep(default_runtime_mins * 60)
    print("end task 2")


@asset
def task_4():
    print("start task 4")
    default_runtime_mins = 3
    time.sleep(default_runtime_mins * 60)
    print("end task 4")


@asset(deps=[task_1, task_4])
def task_3():
    print("start task 3")
    default_runtime_mins = 1.5
    time.sleep(default_runtime_mins * 60)
    print("end task 3")


@asset(deps=[task_3, task_4])
def task_5():
    print("start task 5")
    default_runtime_mins = 2
    time.sleep(default_runtime_mins * 60)
    print("end task 5")


@asset(deps=[task_2, task_3])
def task_6():
    print("start task 6")
    default_runtime_mins = 0.3
    time.sleep(default_runtime_mins * 60)
    print("end task 6")


@asset(deps=[task_5, task_6, task_3])
def task_7():
    print("start task 7")
    default_runtime_mins = 4
    time.sleep(default_runtime_mins * 60)
    print("end task 7")
