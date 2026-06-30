import sys
import os
sys.path.append("/opt/airflow")

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta , datetime
from include.python.process_monthly_data import process_monthly_data



default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes =5)
    }
with DAG(
    dag_id="nyc_taxi_pipeline",
    default_args=default_args,
    description="NYC Taxi ETL Pipeline",
    start_date=datetime(2026, 1,1),
    schedule=None,
    catchup=False

) as dag:
    for month in range(1, 13):

        Process_monthly_data=PythonOperator(
            task_id=f"process_2023_{str(month).zfill(2)}",
            python_callable=process_monthly_data,
            op_kwargs={
                "year": 2023,
                "month": month
            }
        )