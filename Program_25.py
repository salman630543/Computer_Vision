import cv2
import numpy as np
image = cv2.imread('C:\\Users\\USER\\OneDrive\\Desktop\\CV\\Pic_4.jpg')
image_float = image.astype(np.float32) / 255.0
mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.float32)
mask[int(image.shape[0] * 0.4):int(image.shape[0] * 0.6), int(image.shape[1] * 0.4):int(image.shape[1] * 0.6)] = 1.0
mask = np.expand_dims(mask, axis=-1)
sharpened = cv2.addWeighted(image_float, 1.0, image_float * mask, 0.5, 0.0)
sharpened = (sharpened * 255.0).astype(np.uint8)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
