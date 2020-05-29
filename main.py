import cv2 as cv
import numpy as np

lower = np.array([255, 255, 255])
upper = np.array([0, 0, 0])

is_clicked = False


def mouse_function(event, x, y, flags, param):
    global hsv, is_clicked, lower, upper
    if event == cv.EVENT_LBUTTONDOWN:
        is_clicked = True
        if hsv[y][x][0] < lower[0]:
            lower[0] = hsv[y][x][0]
        elif hsv[y][x][0] > upper[0]:
            upper[0] = hsv[y][x][0]

        if hsv[y][x][1] < lower[1]:
            lower[1] = hsv[y][x][1]
        elif hsv[y][x][1] > upper[1]:
            upper[1] = hsv[y][x][1]

        if hsv[y][x][2] < lower[2]:
            lower[2] = hsv[y][x][2]
        elif hsv[y][x][2] > upper[2]:
            upper[2] = hsv[y][x][2]
        print(hsv[y][x])


cap = cv.VideoCapture(0)

cv.namedWindow('Video')
cv.namedWindow('Result')
cv.setMouseCallback('Video', mouse_function)

if cap.isOpened():
    print('camera opened')

    while True:
        _, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        if is_clicked:
            result = cv.inRange(hsv, lower, upper)
            cv.imshow('Result', result)
        cv.imshow('Video', frame)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
cap.release()
