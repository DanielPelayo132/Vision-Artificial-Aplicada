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
    cv2.imshow('Mask',mascara)
#Metodo laplaciano
    laplaciano=cv2.Laplacian(frame,cv2.CV_64F)
    cv2.imshow('Laplacian',laplaciano)
#Metodo sobel x
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    cv2.imshow('Sobel_x',sobelx)
#Metodo sobel y
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    cv2.imshow('Sobel_y',sobely)
#Metodo de canny
    bordes=cv2.Canny(frame,100,200)
    cv2.imshow('Bordes',bordes)

    if cv2.waitKey(1)&0xFF==ord('c'):
        break
cv2.destroyAllWindows()
captura.release()