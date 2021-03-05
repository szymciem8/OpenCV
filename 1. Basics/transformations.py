import cv2 as cv
import os

img = cv.imread(os.getcwd() + "\Photos\park.jpg")
cv.imshow('Boston', img)

#Translation -> shifting
def translate(img, x, y):
    transMat = np.float32

cv.waitKey(0)