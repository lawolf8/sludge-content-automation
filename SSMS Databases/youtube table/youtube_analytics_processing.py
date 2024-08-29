from concurrent.futures import ThreadPoolExecutor
import logging
from validation import validate_entry

# Process data in parallel
def process_data_in_batches(data, batch_size=100):
    with ThreadPoolExecutor() as executor:
        batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
        futures = [executor.submit(process_batch, batch) for batch in batches]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                logging.error(f"Error processing batch: {e}")

# Validate and prepare batch
def process_batch(batch):
    valid_entries = []
    for entry in batch:
        if validate_entry(entry):
            video_id = entry['VideoId']
            title = entry['Title']
            url = entry['URL']
            view_count = entry['ViewCount']
            published_at = datetime.strptime(entry['PublishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            valid_entries.append((video_id, title, url, view_count, published_at))
        else:
            logging.warning(f"Skipped invalid entry: {entry}")
    return valid_entries