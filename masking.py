import cv2 as cv
import numpy as np

img = cv.imread("cat.jpeg")
cv.imshow("Source",img)

# NOTE: THE DIMENSIONS OF THE MASK HAVE TO BE THE SAME SIZE AS OF THE IMAGE
blank = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("BLANK IMAGE",blank)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1 )
cv.imshow("Mask",mask) 

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked",masked)

cv.waitKey(0)