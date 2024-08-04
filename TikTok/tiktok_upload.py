import pyautogui
import time

class TikTokUploader:
    def __init__(self):
        pass

    def upload_video(self, video_path, caption):
        # Open TikTok app (make sure TikTok app is already installed and pinned on the taskbar)
        pyautogui.hotkey('win', 's')
        pyautogui.write('TikTok', interval=0.1)
        pyautogui.press('enter')
        time.sleep(5)  # Wait for the app to open

        # Navigate to upload section (coordinates will vary)
        pyautogui.click(x=100, y=200)  # Click on upload button
        time.sleep(5)

        # Click on the file upload input (coordinates will vary)
        pyautogui.click(x=200, y=300)  # Click to open file dialog
        time.sleep(2)
        pyautogui.write(video_path)
        pyautogui.press('enter')
        time.sleep(5)  # Wait for upload

        # Write caption (coordinates will vary)
        pyautogui.click(x=300, y=400)  # Click on caption field
        pyautogui.write(caption, interval=0.1)
        time.sleep(2)

        # Click submit (coordinates will vary)
        pyautogui.click(x=400, y=500)  # Click to submit
        time.sleep(5)

# Example usage:
if __name__ == "__main__":
    video_path = rf"C:\Users\Luke Wolf\Downloads\Output Downloads\stacked_split_screen_20240804105817_part_1.mp4"
    caption = 'Your video caption with hashtags #example #upload'

    uploader = TikTokUploader()
    uploader.upload_video(video_path, caption)