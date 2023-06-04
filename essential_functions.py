import cv2 as cv
 
src_img = cv.imread("sample_image.jpeg")
cv.imshow("image",src_img)
# 1. Converting to grayscale-->
gray = cv.cvtColor(src_img,cv.COLOR_BGR2GRAY)
cv.imshow("GrayscaleImage",gray)

# 2. BLURRING the image-->
blur = cv.GaussianBlur(src_img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blurred_Image",blur)

# 3. Creating Edge Cascade-->
canny = cv.Canny(src_img, 125, 175)
cv.imshow("edges",canny)

# 4. We can pass blur image also to get edges less-->
canny = cv.Canny(blur, 125, 175)
cv.imshow("edges",canny)

# 5. Dilating the image using specific structuring element->in this example we're taking canny as a structured element
dilated = cv.dilate(canny,(7,7),iterations=1)   # It'll shown edges darker than canny.
cv.imshow("Dilated",dilated)

# 6. Eroding--> To get edge cascade back.
eroded = cv.erode(dilated,(7,7),iterations=1)
cv.imshow("Eroded",eroded)

# 7. Resizing image-->
resized = cv.resize(src_img,(500,500))
cv.imshow("Resized",resized)

# 8. Cropping Image--> Using slicing the pixel array.
cropped = src_img[100:250,200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)