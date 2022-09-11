import cv2
import numpy as np

captura=cv2.VideoCapture(0)
while(1):
    _,frame=captura.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    rojo_inferior=np.array([30,150,100])
    rojo_superior=np.array([255,255,180])
    
    mascara=cv2.inRange(hsv,rojo_inferior,rojo_superior)
    resultado=cv2.bitwise_and(frame,frame,mask=mascara)

    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mascara)
    cv2.imshow('Result',resultado)
    
    if cv2.waitKey(1)&0xFF==ord('c'):
        break

cv2.destroyAllWindows()
captura.release()