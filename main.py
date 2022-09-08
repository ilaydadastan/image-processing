import cv2

image = cv2.imread('road.jpeg') # Reading an image


h, w = image.shape[:2]
"""
print(h, w)

blue_channel = image[100, 100, 0]  # Extracting the RGB values of a pixel
print(blue_channel)



roi = image[100:500, 200:300] #Extracting the Region of Interest (ROI)


resize = cv2.resize(image, (800, 800))

ratio = 800 / w  # Calculating the ratio


# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)

"""

#Rotating the Image


center = (w // 2, h // 2) # Calculating the center of the image


matrix = cv2.getRotationMatrix2D(center, -45, 1.0) # Generating a rotation matrix


rotated = cv2.warpAffine(image, matrix, (w, h)) # Performing the affine transformation









