import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg")
cv.imshow("Source",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAYSCALE",gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("Grayscale intensity histogram")
plt.xlabel("Intensity of pixels")
plt.ylabel("no. of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)