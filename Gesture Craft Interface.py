import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import subprocess
import os

# Define the functions to run the scripts

def start_virtual_mouse():
    subprocess.Popen(["python", "D:\GESTURE CRAFT PROJECT\VOLUME UP\DOWN GESTURE Folder\VirtualMouse.py"])

def show_gesture_description():
    desc_window = tk.Toplevel(app)
    desc_window.title("Gesture Descriptions")
    desc_window.geometry("400x300")
    gestures = """
    Gesture Descriptions:
    1. Virtual Mouse:
       - Index Finger Up: Move Cursor
       - Index and Middle Finger Up: Click

    2. Volume Control:
       - Thumb and Index Finger Pinch: Adjust Volume

    3. Image Zooming:
       - Both Index and Thumb Pinch: Zoom In/Out

    4. Go to Desktop:
       - Use Virtual Mouse to control desktop applications
    """
    label = tk.Label(desc_window, text=gestures, justify=tk.LEFT)
    label.pack()

def start_volume_control():
    subprocess.Popen(["python", "D:\GESTURE CRAFT PROJECT\VOLUME UP\DOWN GESTURE Folder\PC VOLUME CONTROL adv.py"])

def start_image_zoom():
    subprocess.Popen(["python", "D:\GESTURE CRAFT PROJECT\ZOOM GESTURE Folder\ZOOM gesture.py"])

def go_to_desktop():
    app.iconify()

# Create the main application window
app = tk.Tk()
app.title("Gesture Control Interface")
app.geometry("800x600")

# Add a canvas to display the video feed
"""canvas = tk.Canvas(app, width=480, height=480)
canvas.pack()"""

# Buttons for different functionalities
btn_gesture_desc = tk.Button(app, text="Gesture Descriptions", command=show_gesture_description)
btn_volume_control = tk.Button(app, text="Volume Control", command=start_volume_control)
btn_image_zoom = tk.Button(app, text="Image Zooming", command=start_image_zoom)
btn_desktop = tk.Button(app, text="Go to Desktop", command=go_to_desktop)

# Place buttons on the window
btn_gesture_desc.pack(pady=10)
btn_volume_control.pack(pady=10)
btn_image_zoom.pack(pady=10)
btn_desktop.pack(pady=10)

# Start the virtual mouse functionality in a separate thread
threading.Thread(target=start_virtual_mouse, daemon=True).start()

# Run the Tkinter main loop
app.mainloop()
