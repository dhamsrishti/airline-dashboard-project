from upload_to_gcs import upload_to_gcs
from load_to_bigquery import load_data_to_bigquery
from data_validation import validate_bigquery_data
from logging_config import setup_logger

logger = setup_logger()

def run_pipeline():
    logger.info("🚀 Starting Airline Delay Pipeline")
    
    # Step 1: Upload to GCS
    if not upload_to_gcs():
        logger.error("GCS Upload Failed. Exiting.")
        return False
    
    # Step 2: Load to BigQuery
    if not load_data_to_bigquery():
        logger.error("BigQuery Load Failed. Exiting.")
        return False
    
    # Step 3: Validate Data
    if not validate_bigquery_data():
        logger.error("Data Validation Failed.")
        return False
    
    logger.info("✅ Pipeline Completed Successfully!")
    return True

if __name__ == "__main__":
    if not run_pipeline():
        raise SystemExit(1)
