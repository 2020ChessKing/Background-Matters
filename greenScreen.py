# Imports
import numpy as np
import cv2

# Starting Variables
video_snapshot = cv2.VideoCapture(0)
image = cv2.imread("./background_image_source.jpg")

# Frames Loop
while True:
    ret, frame = video_snapshot.read()
    print(frame)

    # Resize
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    # Colour Gradient
    upper_bound_black = np.array([104, 153, 70])
    lower_bound_black = np.array([30, 30, 0])

    # Create Mask
    mask = cv2.inRange(frame, lower_bound_black, upper_bound_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Np.Where()
    f = frame - res
    f = np.where(f == 0, image, f)

    # Display Videos
    cv2.imshow("Geniune Video", frame)
    cv2.imshow("Modified Video", f)

    # Loop Break Command
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_snapshot.release()
cv2.destroyAllWindows()
