import cv2 as cv

img = cv.imread("sample_image.jpeg")
cv.imshow("Source_Img",img)

# 1. BGR to GRAYSCALE 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# 2. BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("BGR->HSV",hsv)

# 3. BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("BGR->LAB",lab)

# 4. BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("BGR->RGB",rgb)

# 5. HSV to BGR
hsv_bgr = cv.cvtColor(img,cv.COLOR_HSV2BGR)
cv.imshow("HSV->BGR",hsv_bgr)

# 6. LAB to BGR
lab_bgr = cv.cvtColor(img,cv.COLOR_LAB2BGR)
cv.imshow("LAB->BGR",lab_bgr)

cv.waitKey(0)