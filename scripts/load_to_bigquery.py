from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {bucket_name}/{destination_blob_name}.")

# Usage
if __name__ == "__main__":
    upload_to_gcs(
        bucket_name="airline-delays-bucket", 
        source_file_name="Airline Dataset Updated - v2.csv", 
        destination_blob_name="raw/airline_delays.csv"
    )
