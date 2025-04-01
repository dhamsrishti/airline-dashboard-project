from google.cloud import bigquery
from logging_config import setup_logger

logger = setup_logger()

def validate_bigquery_data():
    """Checks if data was loaded correctly."""
    client = bigquery.Client()
    query = """
        SELECT 
            COUNT(*) as total_rows,
            SUM(CASE WHEN Flight_Status = 'Delayed' THEN 1 ELSE 0 END) as delayed_count
        FROM `my_airline_dataset.airline_delays`
    """
    
    try:
        result = client.query(query).result()
        for row in result:
            logger.info(f"Total Rows: {row['total_rows']}")
            logger.info(f"Delayed Flights: {row['delayed_count']}")
        return True
    except Exception as e:
        logger.error(f"❌ Data validation failed: {e}")
        return False
