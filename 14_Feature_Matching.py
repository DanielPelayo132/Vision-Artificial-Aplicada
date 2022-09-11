import cv2
import matplotlib.pyplot as plt

imagen1=cv2.imread('reach2.jpg',0)
imagen2=cv2.imread('reach_template.jpg',0)
orb=cv2.ORB_create()
kp1,des1=orb.detectAndCompute(imagen1,None)
kp2,des2=orb.detectAndCompute(imagen2,None)
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
coincidencias=bf.match(des1,des2)
coincidencias=sorted(coincidencias,key=lambda x:x.distance)
imagen3=cv2.drawMatches(imagen1,kp1,imagen2,kp2,coincidencias[:10],None, flags=2)
plt.imshow(imagen3)
plt.show()