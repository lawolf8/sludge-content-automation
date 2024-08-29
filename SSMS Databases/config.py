import os

DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
JSON_FILE_PATH = os.getenv('JSON_FILE_PATH', 'path_to_your_json_file.json')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'data_pipeline.log')