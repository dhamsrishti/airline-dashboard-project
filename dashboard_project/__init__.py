"""Airline Dashboard Project main package."""
from .version import __version__  # Optional version tracking

# List what should be available when importing the package
__all__ = [
    'upload_to_gcs',
    'load_to_bigquery',
    'data_validation',
    'main'
]

# Optional package initialization code
print(f"Initializing airline-dashboard-project package (version {__version__})")
