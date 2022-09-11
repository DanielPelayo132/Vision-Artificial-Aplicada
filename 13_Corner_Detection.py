import numpy as np
import cv2

image=cv2.imread('ghost.jpg')
gris=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gris=np.float32(gris)

esquinas=cv2.goodFeaturesToTrack(gris,100,0.01,10)
esquinas=np.int0(esquinas)
for esquinas in esquinas:
    x,y=esquinas.ravel()
    cv2.circle(image,(x,y),3,255,-1)

cv2.imshow('esquinas',image)
cv2.waitKey(0)
cv2.destroyAllWindows()