CREATE OR REPLACE TABLE nyc_taxi_mart.dim_date AS

SELECT
    CAST(FORMAT_DATE('%Y%m%d', dt) AS INT64) AS date_key,
    dt AS full_date,
    EXTRACT(DAY FROM dt) AS day_number,
    FORMAT_DATE('%A', dt) AS day_name,
    EXTRACT(ISOWEEK FROM dt) AS week_number,
    EXTRACT(MONTH FROM dt) AS month_number,
    FORMAT_DATE('%B', dt) AS month_name,
    EXTRACT(QUARTER FROM dt) AS quarter,
    EXTRACT(YEAR FROM dt) AS year,

    CASE
        WHEN EXTRACT(DAYOFWEEK FROM dt) IN (1, 7)
        THEN TRUE
        ELSE FALSE
    END AS is_weekend

FROM UNNEST(
    GENERATE_DATE_ARRAY('2020-01-01', '2030-12-31')
) AS dt;