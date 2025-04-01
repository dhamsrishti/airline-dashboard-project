def setup_logger():
    import logging
    from pathlib import Path
    
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/pipeline.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def setup_logging():  # Add this if referenced in upload_to_gcs.py
    return setup_logger()
