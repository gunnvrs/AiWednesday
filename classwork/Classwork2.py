# Workshop “Drawing Circle on Image”
import numpy as np
import cv2 as cv

#create empty image
img = np.zeros([200, 300], dtype=np.uint8)

# Center coordinates and radius of the circle
center = (150, 100)
radius = 50

# Loop over the pixels and set the values within the circle to 255 (white)
for y in range(200):
    for x in range(300):
        if np.sqrt((x - center[0])**2 + (y - center[1])**2) <= radius:
            img[y, x] = 255

# display the image
cv.imshow("Drawing", img)

# wait for a key press
cv.waitKey(0)

# clean up
cv.destroyAllWindows()