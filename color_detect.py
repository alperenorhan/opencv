import cv2
import numpy as np
import imutils


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('Trackbar')
cv2.createTrackbar('LowH', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('HighH', 'Trackbar', 179, 179, nothing)
cv2.createTrackbar('LowS', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('HighS', 'Trackbar', 255, 255, nothing)
cv2.createTrackbar('LowV', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('HighV', 'Trackbar', 255, 255, nothing)

while 1:
    _, frame = cap.read()
    frame = imutils.resize(frame, 300, 300)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get Trackbar Positions
    ilowH = cv2.getTrackbarPos('LowH', 'Trackbar')
    ihighH = cv2.getTrackbarPos('HighH', 'Trackbar')
    ilowS = cv2.getTrackbarPos('LowS', 'Trackbar')
    ihighS = cv2.getTrackbarPos('HighS', 'Trackbar')
    ilowV = cv2.getTrackbarPos('LowV', 'Trackbar')
    ihighV = cv2.getTrackbarPos('HighV', 'Trackbar')

    lower_red = np.array([ilowH, ilowS, ilowV])
    upper_red = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    frame = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()
