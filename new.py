import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7)
startDist = None
scale = 0
cx, cy = 500, 500

# Specify the correct file path for your image
image_path = "1.jpg"

try:
    img1 = cv2.imread(image_path)
    if img1 is None:
        raise Exception("Image file not found or cannot be read.")
except Exception as e:
    print(f"Exception: {e}")
    exit()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

            if startDist is None:
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                startDist = length

            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length - startDist) // 2)
            cx, cy = info[4:]
            print("Scale:", scale)

    else:
        startDist = None

    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
        img1_resized = cv2.resize(img1, (newW, newH))
        print("Resized Image shape:", img1_resized.shape)

        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1_resized
    except Exception as e:
        print(f"Exception: {e}")

    cv2.imshow("Image", img)
    cv2.waitKey(1)

