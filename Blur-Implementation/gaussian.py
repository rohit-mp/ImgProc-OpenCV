import numpy as np
import cv2

img=cv2.imread('beach.jpg',1)
img1=img
gblur=np.matrix([[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]])
row,col=img.shape[:2]
for i in range(2,row-2):
    for j in range(2,col-2):
        value=0
        for x in range(0,5):
            for y in range(0,5):
                value+=img[i-2+x,j-2+y].astype('float32')*gblur[x,y]
        img1[i,j]=(value/115).astype('uint8')
cv2.imwrite('beach-gaussian-blur.jpg',img1)
cv2.imshow('beach-gaussian-blur',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
