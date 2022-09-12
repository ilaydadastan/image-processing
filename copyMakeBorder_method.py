import cv2

path = r'/Users/ilaydadastan/PycharmProjects/image-processing/road.jpeg'

image = cv2.imread(path)

window_name = 'image'

image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)

cv2.imshow(window_name, image)
cv2.waitKey(0)