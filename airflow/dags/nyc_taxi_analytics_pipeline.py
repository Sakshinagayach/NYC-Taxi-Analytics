from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.operators.empty import EmptyOperator

PROJECT_ID = "project-a620e746-8057-4f13-999"

# =====================================================
# SQL PATHS
# =====================================================

SQL_BASE_PATH = "/opt/airflow/include/sql/analytics/"

BEHAVIORAL_ANALYTICS_SQL_PATH = SQL_BASE_PATH + "Behavioral_analytics.sql"
DAILY_SUMMARY_KPI_SQL_PATH = SQL_BASE_PATH + "daily_summary_KPI.sql"
EFFICIENCY_ANALYTICS_SQL_PATH = SQL_BASE_PATH + "Efficiency_Analytics.sql"
HOURLY_DEMAND_SUMMARY_SQL_PATH = SQL_BASE_PATH + "Hourly_demand_Summary.sql"
PEAK_REVENUE_HOUR_SQL_PATH = SQL_BASE_PATH + "Peak_revenue_hour.sql"
TOP_PICKUP_LOCATIONS_SQL_PATH = SQL_BASE_PATH + "top_pickup_locations.sql"
TOP_PROFITABLE_ROUTES_SQL_PATH = SQL_BASE_PATH + "top_profitable_routes.sql"


# =====================================================
# SAFE SQL LOADER
# =====================================================

def load_sql(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise Exception(f"❌ Failed to load SQL file: {path} | Error: {e}")


# =====================================================
# READ SQL FILES
# =====================================================

behavioral_analytics_sql = load_sql(BEHAVIORAL_ANALYTICS_SQL_PATH)
daily_summary_kpi_sql = load_sql(DAILY_SUMMARY_KPI_SQL_PATH)
efficiency_analytics_sql = load_sql(EFFICIENCY_ANALYTICS_SQL_PATH)
hourly_demand_summary_sql = load_sql(HOURLY_DEMAND_SUMMARY_SQL_PATH)
peak_revenue_hour_sql = load_sql(PEAK_REVENUE_HOUR_SQL_PATH)
top_pickup_locations_sql = load_sql(TOP_PICKUP_LOCATIONS_SQL_PATH)
top_profitable_routes_sql = load_sql(TOP_PROFITABLE_ROUTES_SQL_PATH)


# =====================================================
# DAG
# =====================================================

with DAG(
    dag_id="nyc_taxi_analytics_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["analytics", "bigquery", "nyc_taxi"],
    description="NYC Taxi Analytics Pipeline (BigQuery Transformations)",
) as dag:

    start = EmptyOperator(task_id="start")

    refresh_behavioral_analytics = BigQueryInsertJobOperator(
        task_id="refresh_behavioral_analytics",
        configuration={
            "query": {
                "query": behavioral_analytics_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )

    refresh_daily_summary_kpi = BigQueryInsertJobOperator(
        task_id="refresh_daily_summary_kpi",
        configuration={
            "query": {
                "query": daily_summary_kpi_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )

    refresh_efficiency_analytics = BigQueryInsertJobOperator(
        task_id="refresh_efficiency_analytics",
        configuration={
            "query": {
                "query": efficiency_analytics_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )

    refresh_hourly_demand_summary = BigQueryInsertJobOperator(
        task_id="refresh_hourly_demand_summary",
        configuration={
            "query": {
                "query": hourly_demand_summary_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )

    refresh_peak_revenue_hour = BigQueryInsertJobOperator(
        task_id="refresh_peak_revenue_hour",
        configuration={
            "query": {
                "query": peak_revenue_hour_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )

    refresh_top_pickup_locations = BigQueryInsertJobOperator(
        task_id="refresh_top_pickup_locations",
        configuration={
            "query": {
                "query": top_pickup_locations_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )

    refresh_top_profitable_routes = BigQueryInsertJobOperator(
        task_id="refresh_top_profitable_routes",
        configuration={
            "query": {
                "query": top_profitable_routes_sql,
                "useLegacySql": False,
            }
        },
        project_id=PROJECT_ID,
        location="asia-south1",
        gcp_conn_id="google_cloud_default",
    )


    # =====================================================
    # DAG FLOW (IMPORTANT FIX)
    # =====================================================

    start >> [
        refresh_behavioral_analytics,
        refresh_daily_summary_kpi,
        refresh_efficiency_analytics,
        refresh_hourly_demand_summary,
        refresh_peak_revenue_hour,
        refresh_top_pickup_locations,
        refresh_top_profitable_routes,
    ]
    