CREATE OR REPLACE TABLE nyc_taxi_analytics.top_profitable_routes 
AS 
SELECT
  concat(
    cast(PULocationID as string),
    '->',
    cast(DOLocationID as string)
  ) as routes, 
  PULocationID,
  DOLocationID,
  count(*) as total_trips,
  round(sum(total_amount),2) as revenue,
  
  avg(total_amount) as fare
from nyc_taxi_staging.yellow_trips_staging
where is_valid = True

group by 
  PULocationID,
  DOLocationID
order by revenue DESC

limit 20
