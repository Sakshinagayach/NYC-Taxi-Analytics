CREATE OR REPLACE TABLE nyc_taxi_mart.fact_table
PARTITION BY pickup_date
CLUSTER BY pickup_location_key, dropoff_location_key, payment_type_key
AS

SELECT

TO_HEX(
    MD5(
        CONCAT(
            CAST(s.VendorID AS STRING),
            CAST(s.tpep_pickup_datetime AS STRING),
            CAST(s.tpep_dropoff_datetime AS STRING),
            CAST(s.PULocationID AS STRING),
            CAST(s.DOLocationID AS STRING)
        )
    )
) AS trip_id,

s.VendorID AS vendor_id,

COALESCE(dd_pickup.date_key, -1) AS pickup_date_key,
COALESCE(dt_pickup.time_key, -1) AS pickup_time_key,

COALESCE(dd_dropoff.date_key, -1) AS dropoff_date_key,
COALESCE(dt_dropoff.time_key, -1) AS dropoff_time_key,

COALESCE(pt.payment_type_key, -1) AS payment_type_key,

COALESCE(dl_pickup.location_key, -1) AS pickup_location_key,
COALESCE(dl_dropoff.location_key, -1) AS dropoff_location_key,

s.passenger_count,
s.trip_distance,

TIMESTAMP_DIFF(
    s.tpep_dropoff_datetime,
    s.tpep_pickup_datetime,
    MINUTE
) AS trip_duration_minutes,

s.fare_amount,
s.extra,
s.mta_tax,
s.tip_amount,
s.tolls_amount,
s.improvement_surcharge,
s.congestion_surcharge,
s.Airport_fee,
s.total_amount,

DATE(s.tpep_pickup_datetime) AS pickup_date

FROM nyc_taxi_staging.yellow_trips_staging AS s

LEFT JOIN nyc_taxi_mart.dim_date dd_pickup
ON DATE(s.tpep_pickup_datetime) = dd_pickup.full_date

LEFT JOIN nyc_taxi_mart.dim_date dd_dropoff
ON DATE(s.tpep_dropoff_datetime) = dd_dropoff.full_date

LEFT JOIN nyc_taxi_mart.dim_time dt_pickup
ON EXTRACT(HOUR FROM s.tpep_pickup_datetime) = dt_pickup.hour_number

LEFT JOIN nyc_taxi_mart.dim_time dt_dropoff
ON EXTRACT(HOUR FROM s.tpep_dropoff_datetime) = dt_dropoff.hour_number

LEFT JOIN nyc_taxi_mart.dim_location dl_pickup
ON s.PULocationID = dl_pickup.location_id

LEFT JOIN nyc_taxi_mart.dim_location dl_dropoff
ON s.DOLocationID = dl_dropoff.location_id

LEFT JOIN nyc_taxi_mart.dim_payment_type pt
ON s.payment_type = pt.payment_code

WHERE s.is_valid = TRUE;
