from dagster import (
    run_status_sensor,
    DagsterRunStatus,
    RunStatusSensorContext,
    define_asset_job,
)
import requests


@run_status_sensor(run_status=DagsterRunStatus.STARTED, minimum_interval_seconds=10)
def report_status_started(context: RunStatusSensorContext):
    dagster_run = context.dagster_run
    dagster_event = context.dagster_event
    response = requests.post(
        "http://localhost:8000/job/status",
        json={
            "job_name": dagster_run.job_name,
            "run_id": dagster_run.run_id,
            "run_config": dagster_run.run_config,
            "status": dagster_run.status.value,
            "step_key": dagster_event.step_key,
            "dagster_event": dagster_event.__str__()
        },
    )
    print(response.text)


# @run_status_sensor(run_status=DagsterRunStatus.CANCELING)
# def report_status_canceling(context: RunStatusSensorContext):
#     pass


# @run_status_sensor(run_status=DagsterRunStatus.FAILURE)
# def report_status_failure(context: RunStatusSensorContext):
#     pass


# # @run_status_sensor(run_status=DagsterRunStatus.MANAGED)
# # def report_status_managed(context: RunStatusSensorContext):
# #     pass


# @run_status_sensor(run_status=DagsterRunStatus.NOT_STARTED)
# def report_status_not_started(context: RunStatusSensorContext):
#     pass


# @run_status_sensor(run_status=DagsterRunStatus.QUEUED)
# def report_status_queued(context: RunStatusSensorContext):
#     pass


# @run_status_sensor(run_status=DagsterRunStatus.STARTED)
# def report_status_started(context: RunStatusSensorContext):
#     pass


# @run_status_sensor(run_status=DagsterRunStatus.STARTING)
# def report_status_starting(context: RunStatusSensorContext):
#     pass


# @run_status_sensor(run_status=DagsterRunStatus.SUCCESS)
# def report_status_success(context: RunStatusSensorContext):
#     pass
