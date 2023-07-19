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


# Spatial Domain
img = cv.imread('pic/fish.jpg', cv.IMREAD_GRAYSCALE)

#--------------- Frequency Domain (2) แปลงภาพ Input ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
img_fft = np.fft.fft2(img)


# ---------------Apply Sobel Filter in the Vertical (1) สร้าง Sobel Filter แบบ Horizontal หรือ Vertical อย่างใดอย่างหนึ่งใน Spatial Domain
filtered_vertical = cv.filter2D(img, -1, sobel_vertical)



# Convert img_fft to a compatible data type
img_fft_shifted = np.fft.fftshift(img_fft)
img_fft_shifted_real = np.abs(img_fft_shifted).astype(np.uint8)

# (3) แปลง Filter Sobel ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
sobel_vertical_fft = np.fft.fft2(sobel_vertical)
sobel_vertical_freq = np.fft.fftshift(sobel_vertical_fft)



#Apply Sobel Filter in the Vertical "Frequency domain" 
filtered_vertical_freq = cv.filter2D(img_fft_shifted_real, -1, sobel_vertical_freq)




# Save the filtered images in the Spatial domain
cv.imwrite('picout/filtered_vertical.png', filtered_vertical)

# Save the filtered images in the Frequency domain
cv.imwrite('picout/filtered_vertical_freq.png', filtered_vertical_freq)