import cv2
import numpy as np
import autopy
import threading
import tkinter as tk
from PIL import Image, ImageTk
import HandTrackingModule as htm  # Assuming HandTrackingModule.py is in the same directory

class VirtualMouse:
    def __init__(self, wCam=640, hCam=480, frameR=100, smoothening=7):
        self.wCam = wCam
        self.hCam = hCam
        self.frameR = frameR
        self.smoothening = smoothening

        self.pTime = 0
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.wCam)
        self.cap.set(4, self.hCam)
        self.detector = htm.handDetector(maxHands=1)
        self.wScr, self.hScr = autopy.screen.size()

    def run(self, canvas):
        while True:
            success, img = self.cap.read()
            if not success:
                continue

            img = self.detector.findHands(img)
            lmList, bbox = self.detector.findPosition(img)
            if len(lmList) != 0:
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]

                fingers = self.detector.fingersUp()

                cv2.rectangle(img, (self.frameR, self.frameR), (self.wCam - self.frameR, self.hCam - self.frameR), (255, 0, 255), 2)

                if fingers[1] == 1 and fingers[2] == 0:
                    x3 = np.interp(x1, (self.frameR, self.wCam - self.frameR), (0, self.wScr))
                    y3 = np.interp(y1, (self.frameR, self.hCam - self.frameR), (0, self.hScr))
                    self.clocX = self.plocX + (x3 - self.plocX) / self.smoothening
                    self.clocY = self.plocY + (y3 - self.plocY) / self.smoothening

                    autopy.mouse.move(self.wScr - self.clocX, self.clocY)
                    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    self.plocX, self.plocY = self.clocX, self.clocY

                if fingers[1] == 1 and fingers[2] == 1:
                    length, img, lineInfo = self.detector.findDistance(8, 12, img)
                    if length < 40:
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                        autopy.mouse.click()

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            canvas.imgtk = imgtk
            canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            canvas.update()

# Function to start the virtual mouse in a thread
def start_virtual_mouse(canvas):
    vm = VirtualMouse()
    vm_thread = threading.Thread(target=vm.run, args=(canvas,))
    vm_thread.daemon = True
    vm_thread.start()

# Create a Tkinter window to initialize the Tkinter environment
root = tk.Tk()
root.withdraw()  # Hide the root window since we don't need it for now

# Create a Tkinter canvas
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Start the virtual mouse functionality in a thread
start_virtual_mouse(canvas)

# Run the Tkinter main loop
root.mainloop()
