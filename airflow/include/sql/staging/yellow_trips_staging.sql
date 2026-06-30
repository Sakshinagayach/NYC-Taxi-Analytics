create or replace table nyc_taxi_staging.yellow_trips_staging
partition by pickup_date
cluster by 
    PULocationID,
    DOLocationID
as 
select
      VendorID,
      tpep_pickup_datetime,
      tpep_dropoff_datetime,

      DATE(tpep_pickup_datetime) as pickup_date,
      EXTRACT(HOUR FROM tpep_pickup_datetime) as pickup_hour,
      passenger_count,
      trip_distance,
      RatecodeID, 
      store_and_fwd_flag, 
      PULocationID, 
      DOLocationID, 
      payment_type, 
      fare_amount, 
      extra, 
      mta_tax, 
      tip_amount, 
      tolls_amount, 
      improvement_surcharge, 
      total_amount, 
      congestion_surcharge, 
      Airport_fee,
      ---FEATURE ENGINNERING
      timestamp_diff(tpep_dropoff_datetime,tpep_pickup_datetime,MINUTE) AS trip_duration_minutes,
      safe_divide(trip_distance, timestamp_diff(tpep_dropoff_datetime,tpep_pickup_datetime,HOUR)) as trip_speed,
      safe_divide(tip_amount,total_amount)*100 as tip_percentage,

      ---validation

    case
        when trip_distance <=0 then false
        when total_amount <0 then false
        when timestamp_diff(tpep_dropoff_datetime,tpep_pickup_datetime,MINUTE)
            <=0 then false
        when safe_divide(tip_amount,total_amount)*100 > 100 then false
        else true
    end as is_valid,

    case 
        when trip_distance <=0 then "Invalid trip distance"
        when total_amount <0 then "Invalid amount"
        when timestamp_diff(tpep_dropoff_datetime,tpep_pickup_datetime,MINUTE)
            <=0 then "Invalid trip duration"
        when safe_divide(tip_amount,total_amount)*100 > 100 then "Invalid tip"
        else "Valid"
    end as validation_reason

    FROM nyc_taxi_raw.yellow_trips_raw_optimized
