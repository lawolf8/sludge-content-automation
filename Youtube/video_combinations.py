"""
Youtube Videos Combination/Stack

Stack the two youtube videos (the top being the main video and the bottom being the game (subway surfer, rainbow 6, etc))
"""

import os, datetime
import moviepy.editor as mp

class VideoStacker:
    def __init__(self, folder_path, output_path):
        self.folder_path = folder_path
        self.output_path = output_path

    def get_most_recent_videos(self, num_files=2):
        # Get all files in the folder and sort them by modification time
        files = sorted(
            [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith(('.mp4', '.mov'))],
            key=os.path.getmtime,
            reverse=True
        )
        # Return the most recent files
        return files[:num_files]

    def create_stacked_split_screen(self, top_video_path, bottom_video_path):
        # Load the video clips
        top_clip = mp.VideoFileClip(bottom_video_path)
        bottom_clip = mp.VideoFileClip(top_video_path)

        # Ensure the videos have the same duration
        if top_clip.duration > bottom_clip.duration:
            top_clip = top_clip.subclip(0, bottom_clip.duration)
        else:
            bottom_clip = bottom_clip.subclip(0, top_clip.duration)

        # Stack the videos vertically using clips_array
        final_clip = mp.clips_array([[top_clip], [bottom_clip]])

        # Write the result to a file with optimized settings
        final_clip.write_videofile(self.output_path, codec="libx264", audio_codec="aac", preset='fast', threads=4)

    def process_videos(self):
        # Get the two most recent videos
        recent_videos = self.get_most_recent_videos()
        if len(recent_videos) < 2:
            print("Not enough videos found.")
        else:
            # Create the stacked split screen video
            self.create_stacked_split_screen(recent_videos[0], recent_videos[1])
            print(f"Stacked split screen video saved to {self.output_path}")

# Example usage:
if __name__ == "__main__":
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    folder_path = os.path.join(os.path.expanduser("~"), "Downloads", "Youtube Downloads")
    output_path = os.path.join(os.path.expanduser("~"), "Downloads", f"stacked_split_screen_{timestamp}.mp4")

    video_stacker = VideoStacker(folder_path, output_path)
    video_stacker.process_videos()
