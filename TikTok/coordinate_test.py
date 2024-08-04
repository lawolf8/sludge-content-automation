import pyautogui
import time
print("Press 'Esc' to stop tracking the mouse position.")

def testing_tiktok_upload():
    try:
        while True:
            # Get the current mouse coordinates
            x, y = pyautogui.position()
            # Print the coordinates
            print(f'X: {x}, Y: {y}', end='\r')

            # Check if the 'Esc' key is pressed
            if pyautogui.hotkey('esc'):
                print('\nTracking stopped.')
                break
    except KeyboardInterrupt:
        print('\nTracking stopped by keyboard interrupt.')

if __name__=="__main__":
    testing_tiktok_upload()
    time.sleep(30)

    # Terminate foo
    testing_tiktok_upload.terminate()
