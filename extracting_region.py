
import cv2

image = cv2.imread('road.jpeg')  # Reading an image

roi = image[100:500, 200:300]  #Extracting the Region of Interest (ROI)


cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()