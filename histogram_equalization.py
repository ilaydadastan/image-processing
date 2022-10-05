import cv2

import numpy as np

image = cv2.imread('road.jpeg')

equ = cv2.equalizeHist(img)

res = np.hstack((img, equ))

cv2.imshow('image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()