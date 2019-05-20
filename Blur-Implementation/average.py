import numpy as np
import cv2

img = cv2.imread('beach.jpg',1)
avg = np.matrix([[1,1,1],[1,1,1],[1,1,1]])
row,col = img.shape[:2]
img1 = img
for i in range(1,row-1):
    for j in range(1,col-1):
        total=0
        for x in range(0,3):
            for y in range(0,3):
                total+=img[i-1+x,j-1+y].astype('float32')*avg[x,y]
        img1[i,j]=(total/9).astype('uint8')
cv2.imwrite('beach-average-blur.jpg',img1)
cv2.imshow('average-blur',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

