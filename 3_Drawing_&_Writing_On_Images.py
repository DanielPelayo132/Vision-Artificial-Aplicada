import numpy as np
import cv2

imagen=cv2.imread('oryx.jpg',cv2.IMREAD_COLOR)
cv2.line(imagen,(100,0),(0,100),(255,0,0),5)
cv2.rectangle(imagen,(600,350),(700,450),(0,0,255),5)
cv2.circle(imagen,(410,380),50,(0,255,0),5)
pts=np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(imagen,[pts],True,(0,255,255),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'Oryx',(150,650),font,6,(0,0,0),13,cv2.LINE_AA)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()