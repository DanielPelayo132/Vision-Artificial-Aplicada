import cv2

imagen=cv2.imread('dante.jpg',cv2.IMREAD_COLOR)
##Cambia un pixel seleccionado de color
imagen[50,50]=[180,180,180]
pixel=imagen[10,10]
print(pixel)
##Cambia un rango de pixeles de color
imagen[30:150,200:300]=[125,125,125]
print(imagen.shape)
print(imagen.size)
print(imagen.dtype)
##Trasladar un grupo de pixeles a otra parte de la imagen
dante=imagen[350:450,600:700]
imagen[350:450,350:450]=dante

cv2.imshow('Imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()