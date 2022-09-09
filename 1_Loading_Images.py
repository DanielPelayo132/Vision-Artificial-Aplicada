import cv2

img = cv2.imread('reloj.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()