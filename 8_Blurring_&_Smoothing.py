import cv2
import numpy as np

captura=cv2.VideoCapture(0)
while(1):
    _,frame=captura.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    rojo_inferior=np.array([30,150,50])
    rojo_superior=np.array([255,255,180])
    
    mascara=cv2.inRange(hsv,rojo_inferior,rojo_superior)
    resultado=cv2.bitwise_and(frame,frame,mask=mascara)
    cv2.imshow('Original',frame)
#Suavizado
    kernel=np.ones((15,15),np.float32)/225
    suavizado=cv2.filter2D(resultado,-1,kernel)
    cv2.imshow('Suavizado',suavizado)
#Difuminado gausanio
    gausiano=cv2.GaussianBlur(resultado,(15,15),0)
    cv2.imshow('Gausiano',gausiano)
#Difuminado mediano
    mediano=cv2.medianBlur(resultado,15)
    cv2.imshow('Mediano',mediano)
#Difuminado bilateral
    bilateral=cv2.bilateralFilter(resultado,15,75,75)
    cv2.imshow('Bilateral',bilateral)
    if cv2.waitKey(1)&0xFF==ord('c'):
        break

cv2.destroyAllWindows()
captura.release()