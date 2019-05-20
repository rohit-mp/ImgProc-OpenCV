import cv2
import numpy as np 
import math

img = cv2.imread('image2.jpg',0).astype('float32')
haar1d = cv2.imread('image2.jpg',0).astype('float32')
haar2d = cv2.imread('image2.jpg',0)
row,col = img.shape

for i in range(0,row):
    for j in range(0,int(col/2)):
        haar1d[i,j] = int((img[i,2*j] + img[i,2*j+1]) / 2)
        haar1d[i,j+int(col/2)] = int((img[i,2*j] - img[i,2*j+1]) / 2)
for j in range(0,col):
    for i in range(0,int(row/2)):
        haar2d[i,j] = int((haar1d[i*2,j] + haar1d[i*2+1,j]) / 2)
        haar2d[i+int(row/2),j] = int((haar1d[i*2,j] - haar1d[i*2+1,j]) / 2)
ret,haar2d = cv2.threshold(haar2d,190,255,cv2.THRESH_TOZERO)
cv2.imshow('haar2d-lossy',haar2d)
cv2.imwrite('haar2d-lossy.jpg',haar2d)
cv2.waitKey(0)
cv2.destroyAllWindows()