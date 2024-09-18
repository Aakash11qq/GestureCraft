import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7)

# Provide the absolute path to the image file
img1 = cv2.imread("d:\GESTURE CRAFT PROJECT\ZOOM GESTURE Folder\image.jpg")

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    # Check if img1 is loaded successfully before attempting to use it
    if img1 is not None:
        img[0:250, 0:250] = img1

    cv2.imshow("Image", img)
    cv2.waitKey(1)
