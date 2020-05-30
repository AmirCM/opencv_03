import cv2 as cv

cv.namedWindow('Original', cv.WINDOW_AUTOSIZE)
cv.namedWindow('Threshold', cv.WINDOW_AUTOSIZE)
cv.namedWindow('Contours', cv.WINDOW_AUTOSIZE)

img = cv.imread('cnt.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, tresh = cv.threshold(gray, 250, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(tresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.imshow('Original', img)
cv.imshow('Threshold', tresh)
cv.drawContours(img, contours, -1, (0, 0, 0), thickness=2)
cv.imshow('Contours', img)
cv.waitKey(0)

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    center = (x + w // 2, y + h // 2)
    print('Area:{} Center: ({}, {})'.format(cv.contourArea(cnt), center[0], center[1]))
    cv.circle(img, center, 5, (255, 0, 0), -1)
    cv.imshow('Contours', img)
    cv.waitKey(0)
