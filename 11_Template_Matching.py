import cv2
import numpy as np

imagen_rgb=cv2.imread('reach2.jpg')
imagen_gris=cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2GRAY)
template=cv2.imread('reach_template.jpg')
template_gris=cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

ancho,alto=template_gris.shape[::-1]
resultado=cv2.matchTemplate(imagen_gris,template_gris,cv2.TM_CCOEFF_NORMED)
threshold=0.4
loc=np.where(resultado>=threshold)
for x in zip(*loc[::-1]):
    cv2.rectangle(imagen_rgb,x,(x[0]+ancho,x[1]+alto),(255,0,0),2)

cv2.imshow('Template matching',imagen_rgb)
cv2.imshow('Template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()