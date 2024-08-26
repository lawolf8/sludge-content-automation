![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen) 

<!-- LOGO -->
<br />
<p align="center">
  <img src="https://user-images.githubusercontent.com/54740007/212677385-8f453f16-06fd-41e2-83a6-8a25d5435418.png" alt="Logo" width="80" height="80">

  <h3 align="center">Sludge-Content-Automation</h3>

  <p align="center">
    Script to download Youtube videos, create stacked videos, upload to TikTok, and track all metrics
    <br />
    </p>
</p>


## About The Project
WORK IN PROCESS | ESTIMATED COMPLETION DATE: 09/08/2024
This project is made with Python 3 and is comprised of 3 aspects.

1. Youtube: This will utilize google APIs, VirusTotal API, and some OS libraries (such as moviepy) to download youtube videos, store metrics, check the downloaded file for viruses, stack videos, and log the videos metrics from Youtube.
2. TikTok: Utilizing the TikTok Desktop App, can upload (and schedule upload) and log metrics from TikTok videos using OS libraries (since you cannot use TikTok's APIs unless you have an app)
3. Database: With the metrics gathered from Youtube and Tiktok, this will all be stored in a database within various tables to be used to determine the best content (which videos get the most views, what hastags have the most traction, etc.)

## Getting Started
To get started you need to have python3 installed. If it is not the case you can download it here : https://www.python.org/downloads/<br><br>


### Installation
Make sure you've already git installed. Then you can run the following commands to get the scripts on your computer:
   ```sh
   git clone https://github.com/lawolf8/sludge-content-automation
   cd sludge-content-automation
   ```
The script only requires the `requests` module, you can install it with this command:
```sh
pip install -r requirements.txt
```
   
## Usage
### Import in your script
You can copy the file `Tiktok_uploader.py` in your project folder and use it like this:
```python
from Tiktok_uploader import uploadVideo

session_id = "7a9f3c5d8f6e4b2a1c9d8e7f6a5b4c3d"
file = "my_video.mp4"
title = "MY SUPER TITLE"
tags = ["Funny", "Joke", "fyp"]
schedule_time = 1672592400

# Publish the video
uploadVideo(session_id, file, title, tags, verbose=True)
# Schedule the video
uploadVideo(session_id, file, title, tags, schedule_time, verbose=True)
```
- `session_id`: Your TikTok *sessionid* cookie.<br>
- `file`: The path to the video you want to upload.<br>
- `title`: The title of your publication (without hashtags).<br>
- `tags`: The list of hashtags you want to add to your post (without `#` symbol). May be empty list `[]`.<br>
- `schedule_time`: The timestamp (in seconds) at which you want to schedule your video.<br>
**Note that you cannot schedule a video more than 10 days in advance.**<br>
**Note that your TikTok *sessionid* cookie needs to be updated every 2 months.**

### With the command line
```
usage: Tiktok_uploader.py [-h] -i SESSION_ID -p PATH -t TITLE [--tags [TAGS ...]] [-s SCHEDULE_TIME]

options:
  -h, --help            show this help message and exit
  -i SESSION_ID, --session_id SESSION_ID
                        Tiktok sessionid cookie
  -p PATH, --path PATH  Path to video file
  -t TITLE, --title TITLE
                        Title of the video
  --tags [TAGS ...]     List of hashtags for the video
  -s SCHEDULE_TIME, --schedule_time SCHEDULE_TIME
                        schedule timestamp for video upload
```                        
The `session_id`, `path` and `title` fields are required.
    
