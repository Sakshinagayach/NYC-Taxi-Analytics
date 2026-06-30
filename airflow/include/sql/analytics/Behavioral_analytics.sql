CREATE OR REPLACE TABLE nyc_taxi_analytics.Behavioral_analytics
AS 
select
case
  when extract(DAYOFWEEK from pickup_date)in (1,7) then "weekend"
  else "weekday"
  end as Day_type,
  count(*) as total_trips,
  avg(total_amount) as fare,
  sum(total_amount) as revenue

from nyc_taxi_staging.yellow_trips_staging
where is_valid = True
Group by Day_type
Order by revenue DESC

