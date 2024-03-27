import cv2
import numpy as np
image = cv2.imread('C:\\Users\\USER\\OneDrive\\Desktop\\CV\\Pic_4.jpg')
image_float = image.astype(np.float32) / 255.0
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
low_freq = cv2.filter2D(image_float, -1, kernel)
A = 1.5
sharpened = cv2.addWeighted(image_float, A - 1, image_float - low_freq, 1.0, 0.0)
sharpened = (sharpened * 255.0).astype(np.uint8)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

