CREATE OR REPLACE TABLE nyc_taxi_analytics.top_pickup_locations
AS
SELECT
  PULocationID,
  COUNT(*) AS total_trips_per_zones,
  sum(total_amount) AS total_revenue
FROM nyc_taxi_staging.yellow_trips_staging
WHERE is_valid = TRUE
GROUP BY PULocationID
ORDER BY total_trips_per_zones asc

LIMIT 20
