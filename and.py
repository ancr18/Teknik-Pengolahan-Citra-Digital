#Ardiyansyah R
#F55120001

import cv2
import numpy as np

img = cv2.imread('ancamanis.jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')

cv2.imshow('Original', img)
cv2.imshow('Blank', blank)

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Masked", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
