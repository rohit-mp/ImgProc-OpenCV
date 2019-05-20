import cv2
import numpy as np

img = cv2.imread('divya.jpg')
#img=cv2.resize(img,None,fx=0.5,fy=0.5)
img1 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
upper_range = np.array([130,255,255],dtype='uint8')
lower_range = np.array([108,0,0],dtype='uint8')
mask = cv2.inRange(img1,lower_range,upper_range)
output = cv2.bitwise_and(img,img,mask=mask)
#cv2.imwrite('output.jpg',output)
cv2.imshow('output',output)
cv2.waitKey(0)

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
gray=cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
mask1=cv2.bitwise_not(mask)
op  =cv2.bitwise_and(gray,gray,mask=mask1)
output1=op+output
cv2.imshow('output1',output1)
cv2.imwrite('output2.jpg',output1)
cv2.waitKey(0)
cv2.destroyAllWindows()
