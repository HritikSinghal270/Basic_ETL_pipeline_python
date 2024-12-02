import sys
import os
import logging

# Add the project root directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src import extract, transform, load, utils

def run_pipeline():
    """
    Run the end-to-end ETL pipeline.
    """
    utils.setup_logging()

    try:
        logging.info("Pipeline started.")
        
        # Step 1: Extract
        raw_data = extract.fetch_data(symbol="AAPL")
        logging.info("Data extraction completed.")
        
        # Step 2: Transform
        transformed_data = transform.clean_data(raw_data)
        logging.info("Data transformation completed.")
        
        # Step 3: Load
        load.load_to_db(transformed_data)
        logging.info("Data loading completed.")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
    finally:
        logging.info("Pipeline ended.")

if __name__ == "__main__":
    run_pipeline()
