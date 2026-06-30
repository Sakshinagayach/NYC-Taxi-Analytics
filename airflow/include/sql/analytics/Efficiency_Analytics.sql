CREATE OR REPLACE TABLE nyc_taxi_analytics.Efficiency_Analytics
AS 
SELECT
    count(*) as total_trip,
    round(avg(trip_speed),2) as average_trip_speed,
    round(avg(trip_duration_minutes),2) as avg_trip_duration

FROM nyc_taxi_staging.yellow_trips_staging
where is_valid = TRUE
group by PULocationID
having average_trip_speed <15
order by average_trip_speed asc

