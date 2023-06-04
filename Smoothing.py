import cv2 as cv

img = cv.imread("sample_image.jpeg")
cv.imshow("ActualImage",img)

# Averaging
average = cv.blur(img , (3,3))
cv.imshow("Averaging",average)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("gauss_blur",gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median_blur",median)

# Bilateral Blurring 
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)