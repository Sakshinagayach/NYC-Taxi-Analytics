from include.python.ingestion.reader import read_parquet_from_gcs
from include.python.cleaning.Cleaner import clean_data
from include.python.cleaning.feature_engineering import feature_engineering
from include.python.validation.Validator import validate_data
from include.python.writer.Writer import write_to_gcs

import logging

BUCKET_NAME = "nyc-taxi-analysis"


def process_monthly_data(year, month):

    logging.info("Starting NYC Taxi Processing Pipeline")

    month_str = str(month).zfill(2)

    file_name = f"yellow_tripdata_{year}-{month_str}.parquet"

    path = (
        f"gs://{BUCKET_NAME}/raw/taxi_trips/"
        f"year={year}/month={month_str}/{file_name}"
    )
    logging.info(f"Reading file: {file_name}")

    df = read_parquet_from_gcs(path)

    if df is None:
        raise Exception(f"Failed to read {file_name}")

    logging.info("Cleaning data")
    df = clean_data(df)

    logging.info("Performing feature engineering")
    df = feature_engineering(df)

    logging.info("Validating data")
    df = validate_data(df)

    logging.info("Writing processed data to GCS")
    write_to_gcs(
        df=df,
        year=year,
        month=month,
        file_name=file_name,
        BUCKET_NAME=BUCKET_NAME
    )


    
    logging.info("Pipeline completed successfully")