from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to gs://{bucket_name}/{destination_blob_name}.")

# Run the function
upload_to_gcs(
    bucket_name="airline-delays-bucket", 
    source_file_name="../data/Airline_Dataset.csv", 
    destination_blob_name="raw/airline_delays.csv"
)
