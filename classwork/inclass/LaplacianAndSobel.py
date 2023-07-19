import numpy as np
import cv2 as cv

img = cv.imread('pic/fish.jpg', cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img, cv.CV_64F,0,1,ksize=5)

print("[Input] type:",img.dtype)
print('[Laplacian] type:', laplacian.dtype)
print('[Sobel X] type:',sobelx.dtype)
print('[Sobel Y] type:',sobely.dtype)

laplacian = cv.normalize(laplacian, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
sobelx = cv.normalize(sobelx, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U )
sobely = cv.normalize(sobely, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U )

cv.imwrite('laplacian.png',laplacian)

cv.imwrite('sobelx.png',sobelx)
cv.imwrite('sobely.png',sobely)

