import cv2
import matplotlib.pyplot as plt
import pyautogui


image: object = cv2.imread("road.jpeg", cv2.IMREAD_COLOR)

cv2.imshow("image", image)  #image = window name ??  #imshow:display image
cv2.waitKey(0)
cv2.destroyAllWindows()

#image.shape ???

plt.imshow(image)
#plt.show()

#how can I get the window name?
"""
windows = pyautogui.getAllWindows()
for window in windows:
    print(window.title)
"""