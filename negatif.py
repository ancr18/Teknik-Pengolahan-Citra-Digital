#Ardiyansyah R
#F55120001

import cv2

img = cv2.imread('ancamanis.jpeg')
negatif = 255 - img

cv2.imshow("Gambar Anc Original", img)
cv2.imshow("Gambar Anc Negatif", negatif)

cv2.waitKey(0)
cv2.destroyAllWindows()