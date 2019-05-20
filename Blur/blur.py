import cv2
import numpy as np 

img = cv2.imread('lena.jpeg',0)

#normal blur
blur  = cv2.blur(img,(5,5))
cv2.imwrite('lena-blur.jpeg',blur)
cv2.imshow('blur',blur)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#gaussian blur
gblur = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite('lena-gaussian-blur.jpeg',gblur)
cv2.imshow('gaussian blur',gblur)
cv2.waitKey(0)

#median blur
mblur = cv2.medianBlur(img,5)
cv2.imwrite('lena-median-blur.jpeg',mblur)
cv2.imshow('median blur',mblur)
cv2.waitKey(0)

cv2.destroyAllWindows()