from google.cloud import bigquery 
import logging
logging.info("starting the loading the file to bigquery ")

PROJECT_ID = "project-a620e746-8057-4f13-999"
DATASET_ID = "nyc_taxi_staging"
TABLE_ID = "yellow_trips_staging"


def load_to_bigquery(year, month):
    try: 
        month_str = str(month).zfill(2) 
        source_uri = ( f"gs://nyc-taxi-analysis/processed/taxi_trips/" 
                    f"year={year}/month={month_str}/" 
                    f"yellow_tripdata_{year}-{month_str}.parquet" )
        table_ref = (f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}")

        client = bigquery.Client(project=PROJECT_ID)
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.PARQUET,
            write_disposition="WRITE_APPEND",
            )
        load_job =client.load_table_from_uri(
            source_uri,
            table_ref,
            job_config =job_config,
        )
        load_job.result()
        logging.info(f"Successfully loaded data into {table_ref}")
    except Exception as e: 
        logging.error( f"Error loading data into BigQuery: {e}" ) 
        raise