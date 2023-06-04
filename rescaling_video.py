import cv2 as cv

# Creating function to rescale frames/images  -->
# we can apply this on existing images,videos and on live vidoes.
def rescaleFrame(frame , scale = 0.2):
    width = int(frame.shape[1] * scale )    # 1 means columns of pixel matrix which resembles width of the image.
    height = int(frame.shape[0] * scale )   # 0 means rows which resembles height of the image.

    dimensions = (width,height)   # storing as a tuple 

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Applying on a video-->

capture = cv.VideoCapture("samplevideo.mp4")  

while True:
    isTrue , frame = capture.read()  
    resized_frame = rescaleFrame(frame)
    cv.imshow("video",frame)
    cv.imshow("resized_video" , resized_frame)    

    if cv.waitKey(20) & 0xFF == ord("d"):  
        break


capture.release()
cv.destroyAllWindows()