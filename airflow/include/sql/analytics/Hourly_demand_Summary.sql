CREATE OR REPLACE TABLE nyc_taxi_analytics.Houry_demand_Summary 
as 
select
   pickup_hour,
   count(*) as total_trips

from nyc_taxi_staging.yellow_trips_staging
where is_valid = TRUE
group by pickup_hour
order by total_trips DESC