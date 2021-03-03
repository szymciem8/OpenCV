import cv2 as cv 
import os 


#Picture
#img = cv.imread(os.getcwd() + "\Photos\cat.jpg")
#cv.imshow("Cat", img)

#Video
capture = cv.VideoCapture(os.getcwd() + "\Videos\dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)