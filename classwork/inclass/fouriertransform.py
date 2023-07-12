import numpy as np
import cv2 as cv

img = cv.imread('pic/initiald2.jpeg',cv.IMREAD_GRAYSCALE)
#cast data type to float32 bit
img = img.astype(np.float32);
#take Fourier transform
imgF = np.fft.fft2(img)
#shift (0,0) to center of image
imgF = np.fft.fftshift(imgF)
#find magnitude & phase
imgReal = np.real(imgF)
imglma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imglma**2)
imgPhs = np.arctan2(imglma, imgReal)
#inverse Fourier transform
imgRealInv = imgMag*np.cos(imgPhs)
imglmaInv = imgMag*np.sin(imgPhs)

imgFInv = imgRealInv + imglmaInv*1j

imgFInv = np.fft.ifftshift(imgFInv)
imgInv = np.fft.ifft2(imgFInv)

imglnv = np.real(imgInv)
imgInv = imgInv.astype(np.uint8);

cv.imwrite('input.png',img)
cv.imwrite('output.png',imgInv)
# display magnitude
imgMag = np.log(1+imgMag)
imgMag = cv.normalize(imgMag,None,0,255,cv.NORM_MINMAX,cv.CV_8U)
cv.imwrite('magnitude.png',imgMag)
