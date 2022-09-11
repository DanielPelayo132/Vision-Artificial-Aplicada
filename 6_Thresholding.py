import cv2

imagen=cv2.imread('carro.jpg')
#threshold de imagen
retval,threshold=cv2.threshold(imagen,12,255,cv2.THRESH_BINARY)
cv2.imshow('Original',imagen)
cv2.imshow('Threshold',threshold)
#threshold de imagen en escala de grises
escalagris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(escalagris,10,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold2',threshold2)
#threshold adaptativo de imangen en escala de grises
th=cv2.adaptiveThreshold(escalagris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('Adaptive threshold',th)
#otsu threshold de imagen en escala de grises
retval3,threshold3=cv2.threshold(escalagris,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold3)
cv2.waitKey(0)
cv2.destroyAllWindows()