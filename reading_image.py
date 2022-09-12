import cv2
import matplotlib.pyplot as plt
import pyautogui


image: object = cv2.imread("road.jpeg", cv2.IMREAD_COLOR)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.imshow(image)


"""
windows = pyautogui.getAllWindows()
for window in windows:
    print(window.title)
"""