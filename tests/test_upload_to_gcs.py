from dashboard_project.upload_to_gcs import upload_to_gcs
from dashboard_project.load_to_bigquery import load_data_to_bigquery  # Add this import
from unittest.mock import patch, MagicMock
import pytest

@patch('google.cloud.storage.Client')
def test_upload_to_gcs_success(mock_client):
    # Setup mock
    mock_bucket = MagicMock()
    mock_client.return_value.bucket.return_value = mock_bucket
    mock_blob = MagicMock()
    mock_bucket.blob.return_value = mock_blob

    # Test
    result = upload_to_gcs("test-bucket", "test-file.csv", "test-destination.csv")
    
    # Assert
    assert result is True
    mock_blob.upload_from_filename.assert_called_once_with("test-file.csv")

@patch('google.cloud.storage.Client')
def test_upload_to_gcs_failure(mock_client):
    mock_client.side_effect = Exception("GCS Error")
    
    with pytest.raises(Exception):
        upload_to_gcs("test-bucket", "test-file.csv", "test-destination.csv")

# Remove these tests as they belong in test_load_to_bigquery.py
# @patch('google.cloud.bigquery.Client')
# def test_load_data_success(mock_client):
#     ...
# 
# @patch('google.cloud.bigquery.Client')
# def test_load_data_failure(mock_client):
#     ...
