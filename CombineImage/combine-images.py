import cv2
import numpy as np

car = cv2.imread('car.jpg',1)
logo = cv2.imread('logo.jpeg',0)
t,thresh = cv2.threshold(logo,127,256,cv2.THRESH_TOZERO)
r = cv2.selectROI(car,False)
x,y=thresh.shape
roi = car[int(r[1]):int(r[1]+x) , int(r[0]):int(r[0]+y)]
newroi = cv2.bitwise_and(roi,roi,mask=thresh)
car[int(r[1]):int(r[1]+x),int(r[0]):int(r[0]+y)] = newroi
cv2.imshow('car-with-logo',car)
cv2.imwrite('car-with-logo.jpg',car)
cv2.waitKey(0)
cv2.destroyAllWindows()

