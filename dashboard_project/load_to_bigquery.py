from google.cloud import bigquery
import yaml
from logging_config import setup_logger  # Absolute import from root

logger = setup_logger()

def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def load_data_to_bigquery():
    config = load_config()
    bq_config = config["bigquery"]
    
    client = bigquery.Client(project=bq_config["project_id"])
    table_ref = f"{bq_config['project_id']}.{bq_config['dataset_id']}.{bq_config['table_id']}"
    
    # Define schema explicitly (better than autodetect)
    schema = [
        bigquery.SchemaField("Departure_Date", "DATE"),
        bigquery.SchemaField("Airport_Name", "STRING"),
        bigquery.SchemaField("Arrival_Airport", "STRING"),
        bigquery.SchemaField("Flight_Status", "STRING"),
    ]
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        schema=schema,
        write_disposition="WRITE_TRUNCATE"  # Overwrite table if exists
    )
    
    try:
        load_job = client.load_table_from_uri(
            bq_config["gcs_uri"], table_ref, job_config=job_config
        )
        load_job.result()
        logger.info(f"✅ Data loaded into {table_ref}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to load data into BigQuery: {e}")
        return False

if __name__ == "__main__":
    success = load_data_to_bigquery()
    if not success:
        raise SystemExit(1)
