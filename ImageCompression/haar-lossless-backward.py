import numpy as np 
import cv2

haar2d = cv2.imread('haar2d-lossless.jpg',0).astype('float32')
haar1d = cv2.imread('haar2d-lossless.jpg',0).astype('float32')
img = cv2.imread('haar2d-lossless.jpg',0)

row,col = img.shape
for j in range(0,col):
    for i in range(0,int(row/2)):
        haar1d[2*i,j] = int( haar2d[i,j] + haar2d[i+int(row/2),j] )
        haar1d[2*i+1,j] = int( haar2d[i,j] - haar2d[i+int(row/2),j] )
for i in range(0,row):
    for j in range(0,int(col/2)):
        img[i,j*2] = int( haar1d[i,j] + haar1d[i,j+int(col/2)] )
        img[i,j*2+1] = int( haar1d[i,j] - haar1d[i,j+int(col/2)] )

cv2.imwrite('haar2d-lossless-inverse.jpg',img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()