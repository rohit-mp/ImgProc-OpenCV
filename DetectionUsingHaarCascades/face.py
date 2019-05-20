import numpy as np 
import cv2

img = cv2.imread('family.jpg')
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
faces = face_cascade.detectMultiScale(img,1.3,7)
eyes = eye_cascade.detectMultiScale(img,1.3,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
for (x,y,w,h) in eyes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow('faces',img)
cv2.imwrite('detected.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
