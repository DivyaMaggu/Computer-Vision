import cv2 as cv

# Creating function to rescale frames/images  -->
def rescaleFrame(frame , scale = 0.2):
    width = int(frame.shape[1] * scale )    # 1 means columns of pixel matrix which resembles width of the image.
    height = int(frame.shape[0] * scale )   # 0 means rows which resembles height of the image.

    dimensions = (width,height)   # storing as a tuple 

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Applying function on single image -->
img  = cv.imread("sample_image.jpeg")     
resized_image = rescaleFrame(img)
cv.imshow("alien",img)     
cv.imshow("new_image",resized_image)

cv.waitKey(0)