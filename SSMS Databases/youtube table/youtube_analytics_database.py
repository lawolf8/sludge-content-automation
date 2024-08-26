import json
import pyodbc
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='data_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database connection setup
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server_name;'
        'DATABASE=YouTubeAnalytics;'
        'UID=your_username;'
        'PWD=your_password'
    )
    cursor = conn.cursor()
    logging.info("Database connection established.")
except Exception as e:
    logging.error(f"Failed to connect to database: {e}")
    raise

# Load JSON data
try:
    with open('path_to_your_json_file.json', 'r') as file:
        data = json.load(file)
    logging.info("JSON data loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load JSON file: {e}")
    raise

# Data validation function
def validate_entry(entry):
    required_keys = {"VideoId", "Title", "URL", "ViewCount", "PublishedAt"}
    if not required_keys.issubset(entry.keys()):
        logging.warning(f"Invalid entry: Missing keys in {entry}")
        return False
    if not isinstance(entry["ViewCount"], int):
        logging.warning(f"Invalid entry: ViewCount is not an integer in {entry}")
        return False
    try:
        datetime.strptime(entry["PublishedAt"], "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        logging.warning(f"Invalid entry: PublishedAt is not a valid datetime in {entry}")
        return False
    return True

# Insert data into the database
for entry in data:
    if validate_entry(entry):
        video_id = entry['VideoId']
        title = entry['Title']
        url = entry['URL']
        view_count = entry['ViewCount']
        published_at = datetime.strptime(entry['PublishedAt'], "%Y-%m-%dT%H:%M:%SZ")

        try:
            # Check if the video already exists
            cursor.execute("SELECT COUNT(1) FROM VideoMetrics WHERE VideoId = ?", video_id)
            if cursor.fetchone()[0] == 0:
                # Insert new entry
                cursor.execute("""
                    INSERT INTO VideoMetrics (VideoId, Title, URL, ViewCount, PublishedAt)
                    VALUES (?, ?, ?, ?, ?)
                """, video_id, title, url, view_count, published_at)
                logging.info(f"Inserted: {title}")
            else:
                logging.info(f"Skipped: {title} (already exists)")
        except Exception as e:
            logging.error(f"Failed to insert entry: {e}")
            continue
    else:
        logging.warning(f"Skipped invalid entry: {entry}")

# Commit and close connection
try:
    conn.commit()
    logging.info("Database transaction committed.")
except Exception as e:
    logging.error(f"Failed to commit transaction: {e}")

cursor.close()
conn.close()
logging.info("Database connection closed.")
