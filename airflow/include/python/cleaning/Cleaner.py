import pandas as pd
import numpy as np
import logging


def remove_null(df):
    critical_columns = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "PULocationID",
        "DOLocationID",
        "payment_type",
        "fare_amount",
        "extra",
        "mta_tax",
        "tip_amount",
        "tolls_amount",
        "improvement_surcharge",
        "total_amount"
    ]

    return df.dropna(subset=critical_columns)


def filter_passenger_count(df):
    # Keep only valid passenger counts
    return df[(df["passenger_count"] >= 1) & (df["passenger_count"] <= 8)]


def filter_total_amount(df):
    return df[df["total_amount"] >= 0]


def filter_trip_distance(df):
    return df[df["trip_distance"] > 0]


def filter_invalid_time(df):
    return df[
        df["tpep_dropoff_datetime"] >=
        df["tpep_pickup_datetime"]
    ]


def clean_data(df):
    logging.info("Starting data cleaning")

    initial_rows = len(df)

    df = remove_null(df)
    df = filter_passenger_count(df)
    df = filter_total_amount(df)
    df = filter_trip_distance(df)
    df = filter_invalid_time(df)

    final_rows = len(df)

    logging.info(
        f"Cleaning completed. Rows before: {initial_rows}, Rows after: {final_rows}"
    )

    return df