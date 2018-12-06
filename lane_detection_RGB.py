import cv2
import numpy as np

def roi(img, square, color3=(255,255,255), color1=255):

    mask = np.zeros_like(img)   #same size with img and set no data

    if len(img.shape) > 2:  #if img with 3ch
        color = color3
    else:                   #if img with 1ch
        color = color1

    cv2.fillPoly(mask, square, color)

    roi_image = cv2.bitwise_and(img, mask)
    #cv2.imshow('roi_image', roi_image)
    return roi_image

def mark_img(img, blue_threshold=200, green_threshold=200, red_threshold=200):

    bgr_thresholds = [blue_threshold, green_threshold, red_threshold]

    thresholds = (img[:,:,0] < bgr_thresholds[0]) |\
                 (img[:,:,1] < bgr_thresholds[1]) |\
                 (img[:,:,2] < bgr_thresholds[2])
    np_img[thresholds] = [0, 0, 0]

    return np_img

img = cv2.imread('road1.jpg')
height, width = img.shape[:2]

square = np.array([[(0,height),(0, height/2), (width, height/2), (width,height)]], dtype=np.int32)
roi_img = roi(img, square)


np_img = np.copy(roi_img)
#cv2.imshow('np_image1', np_img)
#cv2.imshow('roi_image1', roi_img)
np_img = mark_img(np_img)
cv2.imshow('np_image2', np_img)

cv2.imshow('roi_white', np_img)
cv2.imshow('result', img)
cv2.waitKey(0)

'''
import cv2
import numpy as np

image = cv2.imread('road.jpg')
np_image = np.copy(image)   #copy image to numpy format

blue_threshold = 200
red_threshold = 200
green_threshold = 200
bgr_threshold = [blue_threshold, green_threshold, red_threshold]

#change black color
thresholds = (image[:,:,0] < bgr_threshold[0]) | \
             (image[:,:,1] < bgr_threshold[1]) | \
             (image[:,:,2] < bgr_threshold[2])
np_image[thresholds] = [0, 0, 0]

### test image list value
#print(image[:,:,0] < bgr_threshold[0])
#print(thresholds)
#print(image)
#print(image[:,:,0])
#print(image[:,:,1])
#print(image[:,:,2])
#print(thresholds)



cv2.imshow('white', np_image)
cv2.imshow('result',image)
cv2.waitKey(0)
'''