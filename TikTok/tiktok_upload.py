import pyautogui
import time
import pygetwindow as gw

class application:
    def __init__(self):
        pass
    def get_screen_size(self):
        screen_width, screen_height = pyautogui.size()
        return screen_width, screen_height

    def center_window(self, window_title):
        windows = gw.getWindowsWithTitle(window_title)
        if not windows:
            raise Exception(f"Window not found: {window_title}")
        
        window = windows[0]
        window_width, window_height = window.width, window.height
        screen_width, screen_height = self.get_screen_size()
        new_left = (screen_width - window_width) // 2
        new_top = (screen_height - window_height) // 2
        window.moveTo(new_left, new_top)
        window.maximize()


class tiktok_automation:
    def __init__(self):
        pass
    def open_tiktok_and_center_and_fullscreen(self):
        pyautogui.hotkey('win', 's')
        pyautogui.write('TikTok', interval=0.1)
        pyautogui.press('enter')
        time.sleep(10)
        application.center_window('TikTok')

    def upload_video(self, video_path, caption):
        # Open TikTok and center the window
        self.open_tiktok_and_center_and_fullscreen()
        time.sleep(5)  # Wait for TikTok to fully load

        # Navigate to the upload section (adjust coordinates)
        pyautogui.moveTo(1650, 50, duration=1)  # Adjust to the upload button
        pyautogui.click()
        time.sleep(3)

        # Click on the file upload input (adjust coordinates)
        pyautogui.moveTo(1060, 465, duration=1)  # Adjust to the file dialog
        pyautogui.click()
        time.sleep(2)

        # Type the path to the video file
        pyautogui.write(video_path)
        pyautogui.press('enter')
        time.sleep(5)  # Wait for the video to be uploaded

        # Write the caption (adjust coordinates)
        pyautogui.moveTo(940, 330, duration=1)  # Adjust to the caption field
        pyautogui.click()
        # delete text somehow
        pyautogui.write(caption, interval=0.1)
        time.sleep(2)

        # Click submit (adjust coordinates)
        pyautogui.moveTo(620, 1020, duration=1)  # Adjust to the submit button
        pyautogui.click()
        time.sleep(5)

if __name__ == "__main__":
    video_path = r"C:\Users\Luke Wolf\Downloads\Output Downloads\stacked_split_screen_20240804105817_part_1.mp4"
    caption = 'Your video caption with hashtags #example #upload'
    
    tiktok_automation.upload_video(video_path, caption)
