import cv2

cascade_cara=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_ojo=cv2.CascadeClassifier('haarcascade_eye.xml')
captura=cv2.VideoCapture(0)

while 1:
    ret,imagen=captura.read()
    gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    caras=cascade_cara.detectMultiScale(gris,1.3,5)
    
    for (x,y,w,h) in caras:
        cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gris=gris[y:y+h,x:x+w]
        roi_color=imagen[y:y+h,x:x+w]

        ojos=cascade_ojo.detectMultiScale(roi_gris)
        for (ex,ey,ew,eh) in ojos:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,255),2)

    cv2.imshow('imagen',imagen)
    if cv2.waitKey(1)&0xFF==ord('c'):
        break

captura.release()
cv2.destroyAllWindows()