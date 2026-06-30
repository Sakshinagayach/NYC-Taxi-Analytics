CREATE OR REPLACE TABLE nyc_taxi_analytics.Peak_revenue_hour AS 
SELECT
      pickup_hour,
      count(*) as total_trips,
      sum(total_amount) as revenue
from nyc_taxi_staging.yellow_trips_staging
where is_valid = TRUE
group by pickup_hour
order by revenue DESC 

