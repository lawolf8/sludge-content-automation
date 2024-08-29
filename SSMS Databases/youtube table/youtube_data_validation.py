import logging
from datetime import datetime

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