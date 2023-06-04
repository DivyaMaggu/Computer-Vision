import cv2 as cv

img  = cv.imread("sample_image.jpeg")     #  this method takes an image path & return the image as a matrix of pixel.
print(img)


cv.imshow("alien",img)     # this method creates a window to show an image.

cv.waitKey(0) # keyboard binding function, it waits for a specific delay or time in milliseconds for a key to be pressed.
 

