import cv2
import os

path = r'/Users/ilaydadastan/PycharmProjects/image-processing/road.jpeg'
directory = r'/Users/ilaydadastan/PycharmProjects/image-processing'

image = cv2.imread(path)   #default mode, grayscale mode:(path, 0)

os.chdir(directory)
print(os.listdir(directory))

filename = 'savedRoad.jpeg'

cv2.imwrite(filename, image)

print(os.listdir(directory))

print('Successfully saved')
