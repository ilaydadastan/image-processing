import matplotlib.pyplot as plt
import cv2

img = plt.imread('new.png')

histr = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histr)
plt.show()