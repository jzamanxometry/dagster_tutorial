from dagster import repository

from hello_cereal import hello_cereal_job
from complex_job import diamond
from configurable_job import configurable_job
from scheduler import every_minute_schedule

@repository
def hello_cereal_repository():
    # Note that we can pass a dict of functions, rather than a list of
    # job definitions. This allows us to construct jobs lazily,
    # if, e.g., initializing a job involves any heavy compute
    return {
        "jobs": {
            "hello_cereal_job": lambda: hello_cereal_job,
            "diamond": lambda: diamond,
            "configurable_job": lambda: configurable_job
        },
        "schedules": {
            "every_minute_schedule": lambda: every_minute_schedule
        }
    }