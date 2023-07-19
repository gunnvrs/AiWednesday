import numpy as np
import cv2 as cv

# Sobel Filter for Horizontal direction
sobel_horizontal = np.array([[-1, -2, -1],
                             [ 0,  0,  0],
                             [ 1,  2,  1]])

# Sobel Filter for Vertical direction
sobel_vertical = np.array([[-1,  0,  1],
                           [-2,  0,  2],
                           [-1,  0,  1]])

img = cv.imread('pic/initiald2.jpeg', cv.IMREAD_GRAYSCALE)


# Apply Sobel Filter in the Horizontal
filtered_horizontal = cv.filter2D(img, -1, sobel_horizontal)

# Apply Sobel Filter in the Vertical 
filtered_vertical = cv.filter2D(img, -1, sobel_vertical)

cv.imwrite('filtered_horizontal.png',filtered_horizontal)
cv.imwrite('filtered_vertical.png',filtered_vertical)

