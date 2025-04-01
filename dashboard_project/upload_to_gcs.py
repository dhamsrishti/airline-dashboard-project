from google.cloud import storage
import yaml
from pathlib import Path
from logging_config import setup_logger as setup_logging

logger = setup_logging()

def load_config():
    config_path = Path("config/settings.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def upload_to_gcs(bucket_name: str, source_file: str, destination_blob: str) -> bool:
    """Uploads a file to Google Cloud Storage."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob)
        
        blob.upload_from_filename(source_file)
        logger.info(f"✅ File {source_file} uploaded to {bucket_name}/{destination_blob}")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to upload to GCS: {e}")
        raise  # Re-raise the exception instead of returning False

if __name__ == "__main__":
    config = load_config()
    gcs_config = config["gcs"]
    
    success = upload_to_gcs(
        bucket_name=gcs_config["bucket_name"],
        source_file=gcs_config["source_file"],
        destination_blob=gcs_config["destination_blob"]
    )
    
    if not success:
        raise SystemExit(1)  # Exit with error code if upload fails
