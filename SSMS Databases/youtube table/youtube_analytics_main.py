import json
import logging
from config import JSON_FILE_PATH, LOG_FILE_PATH
from database import get_connection, upsert_data
from processing import process_data_in_batches

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load JSON data
try:
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)
    logging.info("JSON data loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load JSON file: {e}")
    raise

# Process data in parallel batches and upsert into database
try:
    conn = get_connection()
    cursor = conn.cursor()
    batches = process_data_in_batches(data)
    for batch in batches:
        upsert_data(cursor, batch)
    conn.commit()
    logging.info("Database transaction committed.")
except Exception as e:
    logging.error(f"Pipeline failed: {e}")
finally:
    cursor.close()
    conn.close()
    logging.info("Database connection closed.")