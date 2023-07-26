import cv2 as cv
import random
from skimage.metrics import structural_similarity as ssim

# Function to add salt-and-pepper noise to the image
def add_salt_and_pepper_noise(img, density_salt, density_pepper):
    height, width = img.shape[:2]

    # Adding salt noise
    number_of_white_pixel = int(density_salt * (height * width))
    for i in range(number_of_white_pixel):
        y_coord = random.randint(0, height - 1)
        x_coord = random.randint(0, width - 1)
        img[y_coord][x_coord] = 255

    # Adding pepper noise
    number_of_black_pixel = int(density_pepper * (height * width))
    for i in range(number_of_black_pixel):
        y_coord = random.randint(0, height - 1)
        x_coord = random.randint(0, width - 1)
        img[y_coord][x_coord] = 0

    return img

# Read the image
img = cv.imread('pic/initiald2.jpeg', cv.IMREAD_GRAYSCALE)

# Define the density of salt-and-pepper noise
density_salt = 0.1
density_pepper = 0.1

# Add salt-and-pepper noise to the image
noisy_img = add_salt_and_pepper_noise(img.copy(), density_salt, density_pepper)

# Apply median filter for noise reduction ####HERE####
filtered_img = cv.medianBlur(noisy_img, 5)

# Calculate the SSIM between the original image and the filtered image
ssim_value, _ = ssim(img, filtered_img, full=True)

# Save the images and SSIM value
cv.imwrite('picout/CW3org.png', img)
cv.imwrite('picout/CW3noisy.png', noisy_img)
cv.imwrite('picout/CW3filtered.png', filtered_img)

# Print the SSIM value
#ปรับ kernel size ให้ได้ใกล้เคียงสุด เช่น 5ใกล้เคียงสุด จาก 3-5-79
print(f'SSIM value between original and filtered image: {ssim_value}')