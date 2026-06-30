from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
GCSToBigQueryOperator,
)
from airflow.providers.google.cloud.operators.bigquery import (
BigQueryInsertJobOperator,
)

PROJECT_ID = "project-a620e746-8057-4f13-999"
BUCKET_NAME = "nyc-taxi-analysis"

# =====================================================

# SQL FILE PATHS

# =====================================================

STAGING_SQL_PATH = (
"/opt/airflow/include/sql/staging/yellow_trips_staging.sql"
)

DIM_DATE_SQL_PATH = (
"/opt/airflow/include/sql/mart/dim_date.sql"
)

DIM_TIME_SQL_PATH = (
"/opt/airflow/include/sql/mart/dim_time.sql"
)

DIM_LOCATION_SQL_PATH = (
"/opt/airflow/include/sql/mart/dim_location.sql"
)

DIM_PAYMENT_TYPE_SQL_PATH = (
"/opt/airflow/include/sql/mart/dim_payment_type.sql"
)

FACT_TABLE_SQL_PATH = (
"/opt/airflow/include/sql/mart/fact_table.sql"
)

# =====================================================

# READ SQL FILES

# =====================================================

with open(STAGING_SQL_PATH, "r") as file:
    staging_sql = file.read()

with open(DIM_DATE_SQL_PATH, "r") as file:
    dim_date_sql = file.read()

with open(DIM_TIME_SQL_PATH, "r") as file:
    dim_time_sql = file.read()

with open(DIM_LOCATION_SQL_PATH, "r") as file:
    dim_location_sql = file.read()

with open(DIM_PAYMENT_TYPE_SQL_PATH, "r") as file:
    dim_payment_type_sql = file.read()

with open(FACT_TABLE_SQL_PATH, "r") as file:
    fact_table_sql = file.read()

# =====================================================

# DAG DEFINITION

# =====================================================

with DAG(
dag_id="nyc_taxi_warehouse_pipeline",
start_date=datetime(2023, 1, 1),
schedule=None,
catchup=False,
tags=["warehouse", "bigquery", "nyc_taxi"],
) as dag:

# =====================================================
# LOAD RAW DATA FROM GCS TO BIGQUERY
# =====================================================

 load_raw_from_gcs = GCSToBigQueryOperator(
    task_id="load_raw_from_gcs",
    bucket=BUCKET_NAME,
    source_objects=[
        "processed/taxi_trips/year=2023/month=01/yellow_tripdata_2023-01.parquet"
    ],
    destination_project_dataset_table=(
        f"{PROJECT_ID}.nyc_taxi_raw.yellow_trips_raw_optimized"
    ),
    source_format="PARQUET",
    write_disposition="WRITE_TRUNCATE",
    create_disposition="CREATE_IF_NEEDED",
    autodetect=True,
    project_id=PROJECT_ID,
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# STAGING
# =====================================================

refresh_staging = BigQueryInsertJobOperator(
    task_id="refresh_staging",
    configuration={
        "query": {
            "query": staging_sql,
            "useLegacySql": False,
        }
    },
    project_id=PROJECT_ID,
    location="asia-south1",
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# DIM DATE
# =====================================================

refresh_dim_date = BigQueryInsertJobOperator(
    task_id="refresh_dim_date",
    configuration={
        "query": {
            "query": dim_date_sql,
            "useLegacySql": False,
        }
    },
    project_id=PROJECT_ID,
    location="asia-south1",
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# DIM TIME
# =====================================================

refresh_dim_time = BigQueryInsertJobOperator(
    task_id="refresh_dim_time",
    configuration={
        "query": {
            "query": dim_time_sql,
            "useLegacySql": False,
        }
    },
    project_id=PROJECT_ID,
    location="asia-south1",
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# DIM LOCATION
# =====================================================

refresh_dim_location = BigQueryInsertJobOperator(
    task_id="refresh_dim_location",
    configuration={
        "query": {
            "query": dim_location_sql,
            "useLegacySql": False,
        }
    },
    project_id=PROJECT_ID,
    location="asia-south1",
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# DIM PAYMENT TYPE
# =====================================================

refresh_dim_payment_type = BigQueryInsertJobOperator(
    task_id="refresh_dim_payment_type",
    configuration={
        "query": {
            "query": dim_payment_type_sql,
            "useLegacySql": False,
        }
    },
    project_id=PROJECT_ID,
    location="asia-south1",
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# FACT TABLE
# =====================================================

refresh_fact_table = BigQueryInsertJobOperator(
    task_id="refresh_fact_table",
    configuration={
        "query": {
            "query": fact_table_sql,
            "useLegacySql": False,
        }
    },
    project_id=PROJECT_ID,
    location="asia-south1",
    gcp_conn_id="google_cloud_default",
)

# =====================================================
# DEPENDENCIES
# =====================================================

load_raw_from_gcs >> refresh_staging

refresh_staging >> [
    refresh_dim_date,
    refresh_dim_time,
    refresh_dim_location,
    refresh_dim_payment_type,
]

[
    refresh_dim_date,
    refresh_dim_time,
    refresh_dim_location,
    refresh_dim_payment_type,
] >> refresh_fact_table