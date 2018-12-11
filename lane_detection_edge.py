import cv2
import numpy as np

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0) # what is sigmaX?

image = cv2.imread('road1.jpg')
height, width = image.shape[:2]

gray_image = grayscale(image)
blur_image = gaussian_blur(image, 3)    #blur setting
canny_image = canny(blur_image, 70, 210)    #recommend 1:2 or 1:3

cv2.imshow("result", canny_img)
cv2.waitKey(0)
