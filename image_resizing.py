
import cv2

image = cv2.imread('road.jpeg') # Reading an image

h, w = image.shape[:2]

resize = cv2.resize(image, (800, 800))


ratio = 800 / w  # Calculating the ratio


# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)