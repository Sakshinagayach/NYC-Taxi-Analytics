from google.cloud import storage
import logging
import os

PROJECT_ID = "project-a620e746-8057-4f13-999"


def write_to_gcs(df, year, month, file_name, BUCKET_NAME):
    tmp_file = None

    try:
        logging.info("Creating temporary parquet file")

        # Create temporary parquet file
        tmp_file = f"/tmp/temp_{year}_{month}.parquet"
        df.to_parquet(tmp_file, index=False)

        logging.info("Initializing GCS client")

        # Initialize GCS client
        client = storage.Client(project=PROJECT_ID)
        bucket = client.bucket(BUCKET_NAME)

        month_str = str(month).zfill(2)

        destination_blob_name = (
            f"processed/taxi_trips/"
            f"year={year}/month={month_str}/{file_name}"
        )

        blob = bucket.blob(destination_blob_name)

        logging.info(
            f"Checking if file already exists: {destination_blob_name}"
        )

        # Check if file already exists
        if blob.exists():
            logging.info(
                f"File {destination_blob_name} already exists in GCS. Skipping upload."
            )
            return

        logging.info(
            f"Uploading file to gs://{BUCKET_NAME}/{destination_blob_name}"
        )

        # Upload file
        blob.upload_from_filename(tmp_file)

        logging.info(
            f"File uploaded successfully to gs://{BUCKET_NAME}/{destination_blob_name}"
        )

    except Exception as e:
        logging.error(f"Error uploading file to GCS: {e}")
        raise

    finally:
        # Remove temporary file
        if tmp_file and os.path.exists(tmp_file):
            os.remove(tmp_file)
            logging.info(f"Temporary file removed: {tmp_file}")