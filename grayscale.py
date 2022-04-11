#Ardiyansyah R
#F55120001

import cv2

img = cv2.imread('ancamanis.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Anc Original", img)
cv2.imshow("Gambar Anc Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()