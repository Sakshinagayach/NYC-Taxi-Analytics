CREATE OR REPLACE TABLE nyc_taxi_mart.dim_time AS

SELECT
    hour AS time_key,
    hour AS hour_number,

    CASE
        WHEN hour BETWEEN 5 AND 11 THEN 'Morning'
        WHEN hour BETWEEN 12 AND 16 THEN 'Afternoon'
        WHEN hour BETWEEN 17 AND 21 THEN 'Evening'
        ELSE 'Night'
    END AS part_of_day,

    CASE
        WHEN hour BETWEEN 7 AND 9
          OR hour BETWEEN 18 AND 20
        THEN TRUE
        ELSE FALSE
    END AS rush_hour_flag

FROM UNNEST(GENERATE_ARRAY(0, 23)) AS hour;