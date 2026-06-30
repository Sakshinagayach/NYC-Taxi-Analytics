CREATE OR REPLACE TABLE nyc_taxi_analytics.daily_summary_KPI
AS
SELECT
  pickup_date,
  COUNT(*) AS total_trips,
  SUM(total_amount) AS total_revenue,
  AVG(total_amount) AS avg_fare_amount,
  AVG(trip_distance) AS avg_trip_distance,
  AVG(trip_duration_minutes) AS avg_trip_duration,
  AVG(tip_percentage) AS avg_tip_percentage

from nyc_taxi_staging.yellow_trips_staging

where is_valid =TRUE
GROUP BY pickup_date
ORDER BY pickup_date
