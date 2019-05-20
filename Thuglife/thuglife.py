import numpy as np 
import cv2

img = cv2.imread('group.jpg')

face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(img,1.3,3)

for (x,y,w,h) in faces:
    eyeFilter = cv2.imread('specs1.png')
    thresh = eyeFilter
    l,b = thresh.shape[:2]
    thresh = cv2.resize(thresh, None, fx=w/b,fy=w/b)
    l,b = thresh.shape[:2]
    mask = cv2.inRange(thresh, np.array([0,0,0]), np.array([100,100,100]))
    thresh = cv2.bitwise_and(thresh,thresh,mask=mask)
    mask = cv2.bitwise_not(mask)
    roi = img[y+int(h/7):y+l+int(h/7),x:x+b]
    output = cv2.bitwise_and(roi,roi,mask=mask)
    mask1 = cv2.inRange(thresh,np.array([0,0,0]),np.array([255,255,255]))
    output = output+thresh
    img[y+int(h/7):y+l+int(h/7),x:x+b] = output

cv2.imshow('img',img)
cv2.imwrite('thuglife.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
