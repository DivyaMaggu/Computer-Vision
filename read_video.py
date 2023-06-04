import cv2 as cv

capture = cv.VideoCapture("samplevideo.mp4")  # take path of the video or zero would reference webcam, 
                               # 1 would reference 1st camera connected to computer.

while True:
    isTrue , frames = capture.read()  # reading the video frame by frame 
    cv.imshow("video" , frames)     # display the video playing.

    if cv.waitKey(20) & 0xFF == ord("d"):  # when letter d is pressed break out of the loop & stop displaying the video.
        break

capture.release()
cv.destroyAllWindows()