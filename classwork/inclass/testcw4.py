import numpy as np
import cv2 as cv

# Sobel Filter for Horizontal direction               1.สร้าง Sobel Filter แบบ Horizontal และ Vertical ใน Spatial Domain ตามที่กำหนดไว้:
sobel_horizontal = np.array([[-1, -2, -1],
                             [ 0,  0,  0],
                             [ 1,  2,  1]])

# Sobel Filter for Vertical direction
sobel_vertical = np.array([[-1,  0,  1],
                           [-2,  0,  2],
                           [-1,  0,  1]])


# Spatial Domain                                        2.แปลงภาพ Input เข้าสู่โดเมนความถี่ (Frequency Domain) โดยใช้ Fourier Transform
img = cv.imread('pic/fish.jpg', cv.IMREAD_GRAYSCALE)

# Frequency Domain
img_fft = np.fft.fft2(img)


# Apply Sobel Filter in the Vertical direction                 5.แปลงภาพผลลัพธ์กลับมาในโดเมน Spatial Domain 
filtered_vertical = cv.filter2D(img, -1, sobel_vertical)


# Convert img_fft to a compatible data type                   4.นำภาพ Input และ Sobel Filter ในโดเมนความถี่มาทำการคูณกันแบบจุดต่อจุด
img_fft_shifted = np.fft.fftshift(img_fft)
img_fft_shifted_real = np.abs(img_fft_shifted).astype(np.uint8)

# Convert sobel_vertical_freq to a compatible data type       3.แปลง Sobel Filter ให้อยู่ในโดเมนความถี่ (Frequency Domain) ด้วย Fourier Transform 
sobel_vertical_freq = sobel_vertical.astype(np.float32)

# Apply Sobel Filter in the Vertical direction in the Frequency domain
filtered_vertical_freq = cv.filter2D(img_fft_shifted_real, -1, sobel_vertical_freq)


# Save the filtered images in the Spatial domain             6.เปรียบเทียบผลลัพธ์ที่ได้ระหว่างการทำ Sobel Filter ใน Spatial Domain และ Frequency Domain
cv.imwrite('picout/filtered_vertical.png', filtered_vertical)

# Save the filtered images in the Frequency domain
cv.imwrite('picout/filtered_vertical_freq.png', filtered_vertical_freq)