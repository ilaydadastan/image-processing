import cv2
import numpy as np

path = r'/Users/ilaydadastan/PycharmProjects/image-processing/road.jpeg'

image = cv2.imread(path)

window_name = 'image'

kernel = np.ones((7, 7), np.uint8)

image = cv2.erode(image, kernel)

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()