import cv2 as cv
import numpy as np

img = cv.imread("sample_image.jpeg")
cv.imshow("img",img)

# Splitting the image -->
b,g,r = cv.split(img)

cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

print(img.shape , b.shape , g.shape , r.shape)

# Merging -->
merged  = cv.merge([b,g,r])
cv.imshow("Merged",merged)

# To show coloured splitted image -->
blank = np.zeros(img.shape[:2],dtype="uint8")
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)