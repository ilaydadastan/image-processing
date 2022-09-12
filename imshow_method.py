import cv2

path = r'/Users/ilaydadastan/PycharmProjects/image-processing/road.jpeg'

image = cv2.imread(path)  #default mode, grayscale mode:(path, 0)

window_name = 'image'

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()