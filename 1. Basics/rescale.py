import cv2 as cv
import os

#This function will work with everything - pictures, videos, lives
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def chage_res(width, height):
    capture.set(3, width)
    capture.set(4, height)

# img = cv.imread(os.getcwd() + '/Photos/cat_large.jpg')
# img = rescale_frame(img, 0.3)
# cv.imshow('Cat', img)

capture = cv.VideoCapture(os.getcwd() + "\Videos\dog.mp4")


while True:
    isTrue, frame = capture.read()
    frame = rescale_frame(frame, 0.2)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)