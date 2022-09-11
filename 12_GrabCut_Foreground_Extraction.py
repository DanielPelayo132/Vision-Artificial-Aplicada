import numpy as np
import cv2
from matplotlib import pyplot as plt

image=cv2.imread('halo.jpg')
mascara=np.zeros(image.shape[:2],np.uint8)

Modelo_fondo=np.zeros((1,65),np.float64)
Modelo_frontal=np.zeros((1,65),np.float64)

rectangulo=(300,100,500,600)
cv2.grabCut(image,mascara,rectangulo,Modelo_fondo,Modelo_frontal,5,cv2.GC_INIT_WITH_RECT)
mascara2=np.where((mascara==2)|(mascara==0),0,1).astype('uint8')
image=image*mascara2[:,:,np.newaxis]

plt.imshow(image)
plt.colorbar()
plt.show()