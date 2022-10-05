
import cv2

# path
path = r'C:\Users\Administrator\Desktop\new.png'

src = cv2.imread(path)

window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )

# Displaying the image
cv2.imshow(window_name, image)
