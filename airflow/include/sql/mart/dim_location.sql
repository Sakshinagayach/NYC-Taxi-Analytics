create table if not exists nyc_taxi_mart.dim_location(
  location_key int64 NOT NULL,
  location_id int64,
  borough STRING,
  zone STRING,
  service_zone string

);
insert into nyc_taxi_mart.dim_location
select
    row_number() over(order by LocationID) as location_key,
    LocationID as location_id ,
    Borough as borough ,
    Zone as zone ,
    service_zone as service_zone

from nyc_taxi_staging.taxi_zone_lookup