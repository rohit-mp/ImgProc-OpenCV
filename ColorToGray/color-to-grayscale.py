import numpy as ny 
import cv2

img = cv2.imread("castle.jpg",1)
cv2.imwrite('castle-mean-formula.jpg',img)
cv2.imwrite('castle-luminosity-formula.jpg',img)
gray1 = cv2.imread('castle-gray1.jpg',1)
gray2 = cv2.imread('castle-gray2.jpg',1)
row,col,color = gray1.shape

#first method - using mean formula
for i in range(0,row):
    for j in range(0,col):
        b,g,r = gray1[i,j]
        gray=(int(r)+int(g)+int(b))/3
        gray1[i,j]=gray
cv2.imshow('castle - grayscale - mean formula',gray1)
cv2.imwrite('castle-mean-formula.jpg',gray1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#second method - using luminosity formula
for i in range(0, row):
    for j in range(0, col):
        b,g,r=gray2[i,j]
        gray=(int(b)*0.07 + int(g)*0.72 + int(r)*0.21)
        gray2[i,j]=gray
cv2.imwrite('castle-luminosity-formula.jpg',gray2)
cv2.imshow('castle - grayscale - luminosity formula',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()