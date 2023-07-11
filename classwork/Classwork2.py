# Workshop “Drawing Circle on Image”
import numpy as np
import cv2 as cv

img = cv.imread('pic/Circle Objects.png')

grayimg = cv.cvtColor(img, cv.IMREAD_GRAYSCALE)

blurimg = cv.medianBlur(grayimg,5)
#หาขอบวงกลม
edges = cv.Canny(blurimg,230,255)

for row in range(0,img.shape[0],3):
    for col in range(0,img.shape[1],3):
        pixel = edges[row, col]
        if pixel > 230:
            radius = 60
            cv.circle(img, (col,row), radius, (0, 255, 0),1)

cv.imshow("Circle",img)
cv.waitKey(0)
cv.destroyAllWindows