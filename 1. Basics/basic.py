import cv2 as cv
import os

#Converting to grayscale
print(os.getcwd())
# img = cv.imread(os.path.join(os.getcwd(), "Photos", "park.jpg"))
img = cv.imread(os.getcwd() + "\Photos\park.jpg")
cv.imshow('Boston', img)

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur", blur)

#Edge cascade
cany = cv.Canny(img, 125, 175)
cv.imshow('Cany', cany)

#Blurred cany
blurred_cany = cv.Canny(blur, 125, 175)
cv.imshow('Blurred Cany', blurred_cany)

cv.waitKey(0)