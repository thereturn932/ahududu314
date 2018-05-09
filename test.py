import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

width = 160
height = 120
minArea = 50


while(True):
    ret, frame = capture.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    sens = 30
    lower_white = np.array([0,0,255-sens], dtype=np.uint8)
    upper_white = np.array([255,sens,255], dtype=np.uint8)

    # Threshold the HSV image to get only white colors
    mask = cv.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    imgErode = cv.erode(mask, None, iterations = 3)
    moments = cv.moments(imgErode, True)

    if moments['m00'] >= minArea:
       x = moments['m10'] / moments['m00']
       y = moments['m01'] / moments['m00']
       print(x, ", ", y)
       cv.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
    
    cv.imshow('frame',hsv)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    cv.imshow("Erosao", imgErode)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
