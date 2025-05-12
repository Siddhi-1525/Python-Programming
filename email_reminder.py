import tkinter as tk
from tkinter import messagebox
import winsound
import time

# Play a beep sound
winsound.Beep(1000, 500)  # 1000 Hz for 0.5 sec

# Create the window (invisible)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show a pop-up reminder
messagebox.showinfo("Reminder", "Don't forget to send an email to Mahek!")

# Keep it open a bit to avoid instant close (optional)
time.sleep(2)
