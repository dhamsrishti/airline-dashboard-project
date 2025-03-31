from unittest.mock import patch, MagicMock
from scripts.upload_to_gcs import upload_to_gcs
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
