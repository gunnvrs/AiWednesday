import numpy as np
import cv2 as cv

def draw_line(img, start_point, end_point, color=(255, 255, 255), thickness=1):
    # Extract the coordinates
    x1, y1 = start_point
    x2, y2 = end_point

    # Calculate the delta values
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the sign of the increments
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Initialize the error values
    error = dx - dy

    # Draw the line
    while x1 != x2 or y1 != y2:
        img[y1, x1] = color

        # Calculate the next pixel coordinates
        error2 = 2 * error
        if error2 > -dy:
            error -= dy
            x1 += sx
        if error2 < dx:
            error += dx
            y1 += sy

# Create a blank image
image = np.zeros((200, 200, 3), dtype=np.uint8)

# Define the start and end points of the line
start_point = (50, 50)
end_point = (150, 150)

# Draw the line on the image
draw_line(image, start_point, end_point, color=(0, 0, 255), thickness=3)

# Display the image
cv.imshow("Line Drawing", image)
cv.waitKey(0)
cv.destroyAllWindows()