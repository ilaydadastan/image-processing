import cv2
import numpy as np

image = cv2.imread('/Users/ilaydadastan/PycharmProjects/image-processing/road.jpeg')

cv2.imshow('original', image)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow(' ', gaussian)
cv2.waitKey(0)

