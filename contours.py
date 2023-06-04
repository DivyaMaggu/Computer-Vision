import cv2 as cv
import numpy as np

img = cv.imread("sample_image.jpeg")
cv.imshow("Source_img",img)

# 1. convert the image to grayscale image -->
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale",gray)

# 2. Blurred image -->
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blurred",blur)

# 3. Edge detection -->
edges = cv.Canny(blur, 125, 175)
cv.imshow("Edges",edges)

# 4. Threshold Function to binarize the image -->
ret , thresh  = cv.threshold(gray , 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

# 5. Finding Contours -->
contours , hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

# Drawing contours on a Blank image -->
blank = np.zeros(img.shape,dtype="uint8")

cv.drawContours(blank,contours,-1, (0,255,0), 1)
cv.imshow("ContoursDrawn",blank)

cv.waitKey(0)

