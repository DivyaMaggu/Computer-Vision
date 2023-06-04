import cv2 as cv
import numpy as np

src_img = cv.imread("sample_image.jpeg")

# 1. Creating a function for Translation -->
def translate(img,x,y):
    trans_mat = np.float32([
                            [1,0,x],
                            [0,1,y]
                            ])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img,trans_mat,dimensions)

translated_img = translate(src_img,100,100)  # -x,-y --> left,up ; x,y --> right,down
cv.imshow("Translation",translated_img)


# 2. Rotation -->

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint == None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)   

rotated_img = rotate(src_img,45)
cv.imshow("Rotation",rotated_img)


# 3. Flipping -->

Flip = cv.flip(src_img,-1)  # 0,1,-1 --> Vertically over y-axis, Horizontally, Vertically & horizontally.
cv.imshow("Flipping",Flip)

cv.waitKey(0)

