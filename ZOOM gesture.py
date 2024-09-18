import cv2
from cvzone.HandTrackingModule import HandDetector
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to choose an image file
def choose_image_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    root.destroy()  # Close the root window
    return file_path

# Function to resize the image while maintaining the aspect ratio
def resize_image(image, scale, max_width, max_height):
    h, w, _ = image.shape
    new_width = int(w * scale)
    new_height = int(h * scale)

    # Ensure the new dimensions fit within the maximum allowed dimensions
    if new_width > max_width:
        new_width = max_width
        new_height = int((max_width / w) * h)
    if new_height > max_height:
        new_height = max_height
        new_width = int((max_height / h) * w)

    return cv2.resize(image, (new_width, new_height))

# Main code
if __name__ == "__main__":
    image_path = choose_image_file()
    if not image_path:
        print("No image selected. Exiting...")
        exit()

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.7)
    startDist = None
    scale = 1
    cx, cy = 640, 360  # Center of the frame

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture video. Exiting...")
            break

        hands, img = detector.findHands(img)
        img1 = cv2.imread(image_path)

        if len(hands) == 2:
            if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
                if startDist is None:
                    length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                    startDist = length

                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                scale = 1 + (length - startDist) / 200  # Adjust the scaling factor as needed

                # Ensure scale is positive
                if scale < 0.1:
                    scale = 0.1
                cx, cy = info[4:]
                print(scale)
        else:
            startDist = None

        try:
            resized_img1 = resize_image(img1, scale, 1280, 720)
            h1, w1, _ = resized_img1.shape

            # Calculate top-left corner of the image to center it
            top_left_x = cx - w1 // 2
            top_left_y = cy - h1 // 2

            # Ensure the coordinates are within the frame dimensions
            if top_left_x < 0:
                top_left_x = 0
            if top_left_y < 0:
                top_left_y = 0
            if top_left_x + w1 > 1280:
                top_left_x = 1280 - w1
            if top_left_y + h1 > 720:
                top_left_y = 720 - h1

            # Overlay the image on the frame
            img[top_left_y:top_left_y + h1, top_left_x:top_left_x + w1] = resized_img1
        except Exception as e:
            print(f"Exception: {e}")
            pass

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

