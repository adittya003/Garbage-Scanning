import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("x"):#millisecon->1
        break

cv2.release()
cv2.destroyAllWindows()

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=np.zeros(frame.shape,dtype=np.uint8)#sgape of frame in previous line
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)#its reducing the image by half
    img[:height//2,:width//2]=smaller_frame#assigning the smaller frame to the top left corner of the image
    img[height//2:,:width//2]=smaller_frame
    img[:height//2,width//2:]=smaller_frame
    img[height//2:,width//2:]=smaller_frame
    cv2.imshow("frame",img)
    if cv2.waitKey(1)==ord("x"):#millisecon->1
        break

cv2.release()
cv2.destroyAllWindows()
#rotate-> cv.rotate(smaller_frame,cv90**)