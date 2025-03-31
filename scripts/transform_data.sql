-- Create a cleaned and optimized table
CREATE OR REPLACE TABLE `my_airline_dataset.clean_airline_delays` AS
WITH flight_stats AS (
  SELECT
    PARSE_DATE('%Y-%m-%d', Departure_Date) AS departure_date,
    Airport_Name AS airport_name,
    Arrival_Airport AS arrival_airport,
    Flight_Status AS flight_status,
    -- Extract useful date parts
    EXTRACT(YEAR FROM PARSE_DATE('%Y-%m-%d', Departure_Date)) AS year,
    EXTRACT(MONTH FROM PARSE_DATE('%Y-%m-%d', Departure_Date)) AS month,
    -- Standardize status values
    CASE 
      WHEN Flight_Status LIKE '%Delay%' THEN 'Delayed'
      WHEN Flight_Status = 'On Time' THEN 'On Time'
      ELSE 'Other'
    END AS standardized_status
  FROM `my_airline_dataset.airline_delays`
  WHERE Flight_Status IS NOT NULL
)

SELECT
  departure_date,
  year,
  month,
  airport_name,
  arrival_airport,
  standardized_status AS flight_status,
  -- Add derived metrics
  COUNT(*) OVER(PARTITION BY airport_name, standardized_status) AS airport_status_count,
  -- Add delay duration if available (example)
  -- delay_minutes / 60 AS delay_hours
FROM flight_stats
WHERE standardized_status IN ('Delayed', 'On Time');
