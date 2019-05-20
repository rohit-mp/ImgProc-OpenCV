import math
import cv2
import numpy as np

img = cv2.imread('rose.jpeg',0).astype('float64')
xkernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
ykernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobelx = cv2.filter2D(img,-1,xkernel)
sobely = cv2.filter2D(img,-1,ykernel)
sobelx=sobelx**2;
sobely=sobely**2;
sobelxy=np.sqrt(sobelx+sobely).astype('uint8')
cv2.imshow('rose-sobel.jpeg',sobelxy)
cv2.imwrite('rose-sobel.jpeg',sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

