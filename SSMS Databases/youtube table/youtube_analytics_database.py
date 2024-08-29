import pyodbc
import logging
from config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD

# Database connection setup
def get_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'DATABASE={DB_NAME};'
            f'UID={DB_USER};'
            f'PWD={DB_PASSWORD}'
        )
        logging.info("Database connection established.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to database: {e}")
        raise

# Upsert data into the database
def upsert_data(cursor, batch):
    upsert_query = """
        MERGE VideoMetrics AS target
        USING (VALUES (?, ?, ?, ?, ?)) AS source (VideoId, Title, URL, ViewCount, PublishedAt)
        ON target.VideoId = source.VideoId
        WHEN MATCHED THEN 
            UPDATE SET Title = source.Title, URL = source.URL, ViewCount = source.ViewCount, PublishedAt = source.PublishedAt
        WHEN NOT MATCHED THEN
            INSERT (VideoId, Title, URL, ViewCount, PublishedAt)
            VALUES (source.VideoId, source.Title, source.URL, source.ViewCount, source.PublishedAt);
    """
    try:
        cursor.executemany(upsert_query, batch)
        logging.info(f"Upserted batch of {len(batch)} records.")
    except Exception as e:
        logging.error(f"Failed to upsert data: {e}")
        raise