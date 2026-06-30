CREATE OR REPLACE TABLE nyc_taxi_mart.dim_payment_type AS

SELECT 1 AS payment_type_key,
1 AS payment_code,
'Credit card' AS payment_name

UNION ALL

SELECT 2, 2, 'Cash'

UNION ALL

SELECT 3, 3, 'No charge'

UNION ALL

SELECT 4, 4, 'Dispute'

UNION ALL

SELECT 5, 5, 'Unknown'

UNION ALL

SELECT 6, 6, 'Voided';
