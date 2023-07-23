import numpy as np
import cv2 as cv

img = cv.imread('pic/fish.jpg', cv.IMREAD_GRAYSCALE)

sobel_horizontal = np.array([[-1, -2, -1],
                             [ 0,  0,  0],
                             [ 1,  2,  1]])

sobel_vertical = np.array([[-1,  0,  1],
                           [-2,  0,  2],
                           [-1,  0,  1]])


#----Fourier_filter----------------------------------------------------------------------------------------------
size = (img.shape[0] - sobel_vertical.shape[0], img.shape[1] - sobel_vertical.shape[1])  
kernel = np.pad(sobel_vertical, (((size[0]+1)//2, size[0]//2), ((size[1]+1)//2, size[1]//2)), 'constant')
kernel = np.fft.ifftshift(kernel)

img = img.astype(np.float32)
imgF = np.fft.fft2(img)
filF = np.fft.fft2(kernel)


#----Dot Product-------------------------------------------------------------------------------------------------
print(img.shape)
dot = imgF * filF 
dotInv = np.fft.ifft2(dot)
dotReal = np.real(dotInv)



#----Result-------------------------------------------------------------------------------------------------------
#ANSWER1  SPATIAL
imgMag = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)  #(0,1) (1,0)  is for vertical and horizontal
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite("picout/CW4_1sobel.png",imgMag)

#ANSWER2  FOURIER
dotInv = cv.normalize(dotReal, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite('picout/CW4_2soble.png', dotInv)