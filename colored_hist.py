import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg")
cv.imshow("Source",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAYSCALE",gray)

# blank = np.zeros(img.shape[:2],dtype="uint8")
# circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

# masked = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow("Mask",masked)

plt.figure()
plt.title("Coloured histogram")
plt.xlabel("Intensity of pixels")
plt.ylabel("no. of pixels")

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)