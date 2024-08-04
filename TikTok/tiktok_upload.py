import pyautogui
import time
import pygetwindow as gw

def get_screen_size():
    screen_width, screen_height = pyautogui.size()
    return screen_width, screen_height

def center_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        raise Exception(f"Window not found: {window_title}")
    
    window = windows[0]
    window_width, window_height = window.width, window.height
    screen_width, screen_height = get_screen_size()
    new_left = (screen_width - window_width) // 2
    new_top = (screen_height - window_height) // 2
    window.moveTo(new_left, new_top)
    window.maximize()

def open_tiktok_and_center_and_fullscreen():
    pyautogui.hotkey('win', 's')
    pyautogui.write('TikTok', interval=0.1)
    pyautogui.press('enter')
    time.sleep(10)
    center_window('TikTok')

def upload_video(video_path, caption):
    # Open TikTok and center the window
    open_tiktok_and_center_and_fullscreen()
    time.sleep(5)  # Wait for TikTok to fully load

    # Navigate to the upload section (coordinates will vary)
    # Adjust these coordinates based on your screen and TikTok's UI
    pyautogui.click(x=1630, y=570)  # Example: Click on the upload button
    time.sleep(3)

    # Click on the file upload input (coordinates will vary)
    pyautogui.click(x=1075, y=475)  # Click to open file dialog
    time.sleep(2)

    # Type the path to the video file
    pyautogui.write(video_path)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the video to be uploaded

    # Write the caption (coordinates will vary)
    pyautogui.click(x=920, y=3444)  # Click on caption field
    pyautogui.write(caption, interval=0.1)
    time.sleep(2)

    # Click submit (coordinates will vary)
    pyautogui.click(x=624, y=1024)  # Click to submit
    time.sleep(5)

if __name__ == "__main__":
    video_path = rf"C:\Users\Luke Wolf\Downloads\Output Downloads\stacked_split_screen_20240804105817_part_1.mp4"
    caption = 'Your video caption with hashtags #example #upload'

    upload_video(video_path, caption)
