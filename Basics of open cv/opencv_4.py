import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    img=cv2.line(frame,(0,0),(width,height),(255,0,0),2)#frame,starting,ending,colour,size
    img=cv2.line(frame,(0,height),(width,0),(0,255,0),2)

    img=cv2.rectangle(frame,(100,100),(200,200),(128,128,128),-1)
    img=cv2.rectangle(frame,(300,300),(500,500),(128,128,128),5)
    
    img=cv2.circle(frame,(400,400),50,(0,0,255),2)
    img=cv2.circle(frame,(400,400),10,(0,0,255),-1)

    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(frame,"Adittya Narayan",(200,height-10),font,1,(0,0,0),5,cv2.LINE_AA)
    cv2.imshow("frame",img)

    if cv2.waitKey(1)==ord("x"):#millisecon->1
        break

cv2.release()
cv2.destroyAllWindows()
