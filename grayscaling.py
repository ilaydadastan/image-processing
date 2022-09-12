import cv2

image = cv2.imread('/Users/ilaydadastan/PycharmProjects/image-processing/road.jpeg')
0
cv2.imshow(' ', image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow(' ', gray_image)
cv2.waitKey(0)

