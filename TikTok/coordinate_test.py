import pyautogui
import keyboard  # Requires the 'keyboard' package

print("Press 'Esc' to stop tracking the mouse position.")

try:
    while True:
        # Get the current mouse coordinates
        x, y = pyautogui.position()
        # Print the coordinates
        print(f'X: {x}, Y: {y}', end='\r')
        
        # Check if the 'Esc' key is pressed
        if keyboard.is_pressed('Esc'):
            print('\nTracking stopped.')
            break
except KeyboardInterrupt:
    print('\nTracking stopped by keyboard interrupt.')