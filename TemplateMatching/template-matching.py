import numpy as np
import cv2

img = cv2.imread('lena-color.png',1)
template = cv2.imread('lena-eyes.png',1)
x,y,channel=template.shape
res = cv2.matchTemplate(img,template,cv2.TM_CCORR_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
cv2.rectangle(img,max_loc,(max_loc[0]+y,max_loc[1]+x),0,5)
cv2.imwrite('detection.png',img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
