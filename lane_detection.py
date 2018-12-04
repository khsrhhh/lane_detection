import cv2
import numpy as np

image = cv2.imread('road.jpg')
np_image = np.copy(image)   #copy image to numpy format

blue_threshold = 200
red_threshold = 200
green_threshold = 200
bgr_threshold = [blue_threshold, green_threshold, red_threshold]

thresholds = (image[:,:,0] < bgr_threshold[0]) | (image[:,:,1] < bgr_threshold[1]) | (image[:,:,2] < bgr_threshold[2])
np_image[thresholds] = [0, 0, 0]

cv2.imshow('white', np_image)
cv2.imshow('result',image)
cv2.waitKey(0)

