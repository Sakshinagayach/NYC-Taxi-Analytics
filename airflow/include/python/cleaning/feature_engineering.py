import pandas as pd
import numpy as np


def add_trip_duration(df):
    # converting into minutes
    df["trip_duration"] = (
        df["tpep_dropoff_datetime"] -
        df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    return df


def add_trip_speed(df):
    df["trip_speed"] = np.where(
        df["trip_duration"] > 0,
        (df["trip_distance"] / (df["trip_duration"] / 60)),
        np.nan
    )

    return df


def add_tip_percentage(df):
    df["tip_percentage"] = np.where(
        df["tip_amount"] > 0,
        (df["tip_amount"] / df["total_amount"]) * 100,
        np.nan
    )

    return df


def add_pickup_hour(df):
    df["pick_hour"] = df["tpep_pickup_datetime"].dt.hour

    return df


def feature_engineering(df):
    df = add_trip_duration(df)
    df = add_trip_speed(df)
    df = add_tip_percentage(df)
    df = add_pickup_hour(df)

    return df