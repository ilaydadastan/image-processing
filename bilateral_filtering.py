import cv2

img = cv2.imread('taj.jpg')

bilateral = cv2.bilateralFilter(img, 15, 75, 75)

cv2.imwrite('taj_bilateral.jpg', bilateral)
