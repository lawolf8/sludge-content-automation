"""
Youtube Video Export

Convert youtube videos to mp4 format with a given url. Additionally, this verifies if the file downloaded by the installer is safe through the VirusTotal API. 

APIs:
VirusTotal (VT) API:
    API KEY: https://docs.virustotal.com/docs/please-give-me-an-api-key
    Request Rate: 4 lookups / min
    Daily Quota: 500 lookups / day
    Monthly Quota: 15.5 k looups / month
"""
from pytubefix import YouTube
import moviepy.editor as mp
import datetime
import random, string, os, requests, time

class YouTubeMP4:
    def __init__(self):
        self.downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads", "Youtube Downloads")
        if not os.path.exists(self.downloads_dir):
            os.makedirs(self.downloads_dir)
            print(f"Created directory: {self.downloads_dir}")
        else:
            print(f"Directory already exists: {self.downloads_dir}")
        #Get the API Key 
        self.username = os.getenv("USERNAME")
        self.api_key = self.read_api_key(rf"C:\\Users\\{self.username}\\Desktop\\API Keys\\VT API Key.txt")

    def read_api_key(self, file_path):
        try:
            with open(file_path, 'r') as file:
                api_key = file.read().strip()
                return api_key
        except Exception as e:
            print(f"Error reading API key from file: {e}")
            return None

    def generate_unique_name(self, base_name):
        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        unique_name = f"{base_name}_{timestamp}_{random_string}.mp4"
        return unique_name

    def youtube_download(self, url):
        try:
            yt = YouTube(url)
            # Check if video requires login
            if yt.age_restricted:
                print("This video is age-restricted and requires login.")
                return
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            filename = self.generate_unique_name(base_name="youtube")
            file_path = os.path.join(self.downloads_dir, filename)
            
            stream.download(output_path=self.downloads_dir, filename=filename)
            video_path = f"{file_path}"

            video = mp.VideoFileClip(video_path)
            output_path = os.path.join(self.downloads_dir, filename)
            video.write_videofile(output_path, codec="libx264")

            print(f"Video downloaded and saved as {output_path}")

            # Verify the file with VirusTotal
            if self.api_key:
                self.verify_file_safety(output_path)

        except Exception as e:
            print(f"Error: {e}")

    def verify_file_safety(self, file_path):
        url = 'https://www.virustotal.com/api/v3/files'

        try:
            with open(file_path, 'rb') as file:
                files = {'file': (os.path.basename(file_path), file)}
                headers = {
                    'x-apikey': self.api_key,
                }
                response = requests.post(url, files=files, headers=headers)
                if response.status_code == 200:
                    json_response = response.json()
                    file_id = json_response['data']['id']
                    print(f"File uploaded to VirusTotal, File ID: {file_id}")
                    self.check_file_safety(file_id)
                else:
                    print(f"Error uploading file to VirusTotal: {response.status_code}")
        except Exception as e:
            print(f"Error verifying file safety: {e}")

    def check_file_safety(self, file_id):
        url = f'https://www.virustotal.com/api/v3/analyses/{file_id}'

        headers = {
            'x-apikey': self.api_key,
        }

        while True:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                json_response = response.json()
                status = json_response['data']['attributes']['status']
                if status == 'completed':
                    results = json_response['data']['attributes']['results']
                    positives = sum(1 for result in results.values() if result['category'] == 'malicious')
                    total = len(results)
                    print(f"File analysis completed: {positives}/{total} detections")
                    break
                else:
                    print("File analysis in progress, waiting for completion...")
                    time.sleep(30)
            else:
                print(f"Error checking file analysis status: {response.status_code}")
                break

#For Testing Purposes 
'''
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=FSvNhxKJJyU"
    youtube_mp4 = YouTubeMP4()
    youtube_mp4.youtube_download(url)
'''