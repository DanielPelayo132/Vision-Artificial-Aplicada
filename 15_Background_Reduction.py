import cv2

captura=cv2.VideoCapture(0)
br=cv2.createBackgroundSubtractorMOG2()

while(1):
    ret,frame=captura.read()

    brmascara=br.apply(frame)
 
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',brmascara)

    if cv2.waitKey(1)&0xFF==ord('c'):
        break  
captura.release()
cv2.destroyAllWindows()