#object or template matching
import cv2
import numpy as np

img=cv2.imread('messi.png',0)
template=cv2.imread('ronaldo.png',0)


h,w=template.shape

methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for method in methods:
    img2=img.copy()

    result= cv2.matchTemplate(img2,template,eval(method))
    #(W-w+1,H-h+1)
    min_val,max_val,min_location,max_location = cv2.minMaxLoc(result)
    #if method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    print(max_location,min_location)
    if method in ['cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']:
        location=min_location
    else:
        location=max_location
    cv2.rectangle(img2,location,(location[0]+w,location[1]+h),255,5)
    cv2.imshow("match",img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


