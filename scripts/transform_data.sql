-- Create a cleaned table
CREATE OR REPLACE TABLE `my_airline_dataset.clean_airline_delays` AS
SELECT 
    "Departure Date",
    "Airport Name",
    "Arrival Airport",
    "Flight Status",
    COUNT(*) OVER(PARTITION BY "Flight Status") AS status_count
FROM `my_airline_dataset.airline_delays`
WHERE "Flight Status" IN ('Delayed', 'On Time');
