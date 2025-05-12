import pyautogui
import datetime
import os

# Create a folder to save screenshots if it doesn't exist
folder_name = "Screenshots"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Generate a unique filename using date and time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = os.path.join(folder_name, f"screenshot_{timestamp}.png")

# Take screenshot
screenshot = pyautogui.screenshot()

# Save screenshot
screenshot.save(filename)

print(f"Screenshot saved as {filename}")
