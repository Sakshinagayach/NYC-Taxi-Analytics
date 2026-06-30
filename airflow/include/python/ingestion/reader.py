import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_parquet_from_gcs(path):
    try:
        logging.info(f"Reading file from: {path}")

        df = pd.read_parquet(
            path,
            engine="pyarrow",
            storage_options={"token": "google_default"}
        )

        logging.info(f"Successfully loaded data. Shape: {df.shape}")

        return df

    except Exception as e:
        logging.error(f"ERROR reading file: {path}")
        logging.error(str(e))

        return None