"""
Youtube Analytics

Utilizing the youtube API, data analytics can be performed to determine most viewed sections of exported videos since the aim is to create a video of a minimum of 1 minute and shorter than 2 due 
to the consumers attention span. Additionally, the data is used to see if the video is considered "worthy" of being uploaded to tiktok based on the attention span, views, and more data metrics.

Mainly, this will be used as part of ratios with tiktok views once videos are posted. The aim is to determine generes, lengths, and so on to determine optimal viewer and follower usage.

Youtube Data API: 
    API KEY: https://developers.google.com/youtube/v3/getting-started
"""

import os
import re
import googleapiclient.discovery
import json
import isodate

class YouTubeMetrics:
    def __init__(self):
        self.username = os.getenv("USERNAME")
        self.api_key = self.read_api_key(rf"C:\\Users\\{self.username}\\Desktop\\API Keys\\Youtube API Key.txt")

        self.youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.api_key)
    def read_api_key(self, file_path):
        try:
            with open(file_path, 'r') as file:
                api_key = file.read().strip()
                return api_key
        except Exception as e:
            print(f"Error reading API key from file: {e}")
            return None
        
    def extract_video_id(self, video_url):
        regex_patterns = [
            r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$',  
            r'(https?://)?(www\.)?(youtube\.com)/shorts/.+$',      
        ]
        for pattern in regex_patterns:
            match = re.match(pattern, video_url)
            if match:
                if "youtu.be" in video_url:
                    return video_url.split('/')[-1]
                elif "youtube.com" in video_url:
                    query = re.split(r'[=&]', video_url)
                    for i in range(len(query)):
                        if query[i].endswith('watch?v'):
                            return query[i + 1]
                        if query[i].endswith('/shorts'):
                            return query[i + 1]
        return None

    def get_video_metrics(self, video_url):
        video_id = self.extract_video_id(video_url)
        if not video_id:
            print("Invalid YouTube URL")
            return None

        request = self.youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=video_id
        )
        response = request.execute()
        
        if "items" not in response or len(response["items"]) == 0:
            print("No video data found.")
            return None
        
        video_data = response["items"][0]
        snippet = video_data["snippet"]
        statistics = video_data["statistics"]
        content_details = video_data["contentDetails"]
        
        duration = isodate.parse_duration(content_details["duration"]).total_seconds()

        metrics = {
            "title": snippet["title"],
            "description": snippet["description"],
            "publishedAt": snippet["publishedAt"],
            "viewCount": statistics.get("viewCount"),
            "likeCount": statistics.get("likeCount"),
            "dislikeCount": statistics.get("dislikeCount"),
            "commentCount": statistics.get("commentCount"),
            "duration": duration
        }
        
        return metrics

    def get_video_watch_time(self, video_id):
        request = self.youtube_analytics.reports().query(
            ids="channel==MINE",
            startDate="2021-01-01",
            endDate="2021-12-31",
            metrics="estimatedMinutesWatched",
            filters=f"video=={video_id}",
            dimensions="day",
            sort="day"
        )
        response = request.execute()

        if "rows" not in response:
            print("No watch time data found.")
            return None

        total_watch_time = sum([float(row[1]) for row in response["rows"]])
        return total_watch_time

    def calculate_watch_time_ratio(self, watch_time, duration):
        if duration == 0:
            return 0
        return watch_time / (duration / 60)

    def print_metrics(self, metrics):
        if metrics:
            print(json.dumps(metrics, indent=4))

#For Testing Purposes 
'''
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=FSvNhxKJJyU"
    
    yt_metrics = YouTubeMetrics()
    metrics = yt_metrics.get_video_metrics(video_url)
    yt_metrics.print_metrics(metrics)
    '''