import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=cv2.imread('beach.jpg',1)
img2=cv2.imread('NITK-Emblem.png',1)

img2=cv2.resize(img2, (0,0), fx=0.75, fy=0.75)
row,col = img2.shape[:2]
img =0.7* img1.astype('float64')
for i in range(0,row):
    for j in range(0,col):
        img[i,j,:]+=img2[i,j,:]*0.4

cv2.imwrite('blendedImage.jpg',img)
cv2.imshow('img',img.astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()
