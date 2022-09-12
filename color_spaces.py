import cv2

image = cv2.imread('road.jpeg')
Blue, Green, Red = cv2.split(image)

cv2.imshow(' ', image)

cv2.imshow("Blue", Blue)
cv2.waitKey(0)

cv2.imshow("Green", Green)
cv2.waitKey(0)

cv2.imshow("Red", Red)
cv2.waitKey(0)


cv2.destroyAllWindows()