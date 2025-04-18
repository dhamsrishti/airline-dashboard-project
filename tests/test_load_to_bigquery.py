from dashboard_project.load_to_bigquery import load_data_to_bigquery
from unittest.mock import patch, MagicMock
import pytest

@patch('google.cloud.bigquery.Client')
def test_load_data_success(mock_client):
    # Setup mock
    mock_job = MagicMock()
    mock_client.return_value.load_table_from_uri.return_value = mock_job

    # Test
    result = load_data_to_bigquery()
    
    # Assert
    assert result is True
    mock_client.return_value.load_table_from_uri.assert_called_once()

@patch('google.cloud.bigquery.Client')
def test_load_data_failure(mock_client):
    mock_client.return_value.load_table_from_uri.side_effect = Exception("BQ Error")
    
    result = load_data_to_bigquery()
    assert result is False
