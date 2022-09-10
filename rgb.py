

import cv2

image = cv2.imread('road.jpeg') # Reading an image


blue_channel = image[100, 100, 0]  # Extracting the RGB values of a pixel
print(blue_channel)

