from dagster import schedule

from hello_cereal import hello_cereal_job

@schedule(
    cron_schedule="*/1 * * * *",
    job=hello_cereal_job,
    execution_timezone="America/New_York",
)
def every_minute_schedule(context):
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {"ops": {"hello_cereal": {"config": {"date": date}}}}