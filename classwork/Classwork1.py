import cv2 as cv
import numpy as np

# สร้างภาพเส้นตรงเป็นฟิลเตอร์
line_filter = np.zeros((5, 5), dtype=np.uint8)
line_filter[2, :] = 255

# โหลดภาพที่ต้องการทดสอบ
image = cv.imread('pic/initiald2.jpeg', cv.IMREAD_GRAYSCALE)

# Convolution ของเส้นตรงกับภาพ
result = cv.filter2D(image, -1, line_filter)

# ปรับค่าสีของผลลัพธ์
result_normalized = cv.normalize(result, None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_8U)

# แสดงผลลัพธ์
cv.imshow("Original Image", image)
cv.imshow("Convolution Result", result_normalized)
cv.waitKey(0)
cv.destroyAllWindows()