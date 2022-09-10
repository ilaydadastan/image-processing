
import cv2

image = cv2.imread('road.jpeg') # Reading an image

h, w = image.shape[:2]

center = (w // 2, h // 2) # Calculating the center of the image


matrix = cv2.getRotationMatrix2D(center, -45, 1.0) # Generating a rotation matrix


rotated = cv2.warpAffine(image, matrix, (w, h)) # Performing the affine transformation
