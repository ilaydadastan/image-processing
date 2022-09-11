import cv2
import numpy as np

image1 = cv2.imread('image1.jpeg')
image2 = cv2.imread('road.jpeg')

subtraction = cv2.subtract(image1, image2)

cv2.imshow(' ', subtraction)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()