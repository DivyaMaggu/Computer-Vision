import cv2 as cv
import numpy as np

# 1. Creating blank image -->
blank = np.zeros((500,500,3),dtype = "uint8")
cv.imshow("Blank_image",blank)

# 2. Paint the image a certain colour -->
# blank[:] = 0,255,0
# cv.imshow("Green",blank)

# 3. Coloured some part of the image -->
# blank[200:300,300:400] = 255,0,0
# cv.imshow("square",blank)

# 4. Draw a Rectangle -->
# cv.rectangle(blank,(0,0),(250,234),(0,255,0),thickness=-1)
# cv.imshow("rectangle",blank)

#  5. Draw a circle -->
# cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
# cv.imshow("circle",blank)
#  6. Draw a line -->
# cv.line(blank,(250,250),(500,500),(255,255,255),thickness=3)
# cv.imshow("line",blank)

#  Write text on an image -->
cv.putText(blank,"Hello Friends!",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("text",blank)


cv.waitKey(0)



