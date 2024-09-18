import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Functionality switch
current_functionality = "Virtual Mouse"

def switch_functionality(new_functionality):
    global current_functionality
    current_functionality = new_functionality
    if new_functionality == "Volume Control":
        subprocess.Popen(['python', 'D:\GESTURE CRAFT PROJECT\VOLUME UP\DOWN GESTURE Folder\PC VOLUME CONTROL adv.py'])
    elif new_functionality == "Image Zooming":
        subprocess.Popen(['python', 'D:\GESTURE CRAFT PROJECT\ZOOM GESTURE Folder\ZOOM gesture.py'])
    elif new_functionality == "Go to Desktop":
        subprocess.Popen(['python', 'D:\GESTURE CRAFT PROJECT\VOLUME UP\DOWN GESTURE Folder\VirtualMouse.py'])
    elif new_functionality == "Gesture Descriptions":
        show_gesture_description()

def show_gesture_description():
    description = """
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
    messagebox.showinfo("Gesture Descriptions", description)

def virtual_mouse():
    subprocess.Popen(['python', 'D:\GESTURE CRAFT PROJECT\VOLUME UP\DOWN GESTURE Folder\VirtualMouse.py'])

def start_interface():
    # Initialize main window
    root = tk.Tk()
    root.title("Gesture Control Interface")
    root.geometry("800x600")

    # Create buttons
    btn_volume_control = tk.Button(root, text="Volume Control", command=lambda: switch_functionality("Volume Control"))
    btn_volume_control.pack()

    btn_image_zooming = tk.Button(root, text="Image Zooming", command=lambda: switch_functionality("Image Zooming"))
    btn_image_zooming.pack()

    btn_descriptions = tk.Button(root, text="Gesture Descriptions", command=lambda: switch_functionality("Gesture Descriptions"))
    btn_descriptions.pack()

    btn_go_to_desktop = tk.Button(root, text="Go to Desktop", command=lambda: switch_functionality("Go to Desktop"))
    btn_go_to_desktop.pack()

    root.mainloop()

# Start Virtual Mouse and Interface
virtual_mouse()
start_interface() 
