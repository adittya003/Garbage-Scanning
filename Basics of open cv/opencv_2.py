import cv2
import random
im=cv2.imread('wallpaperflare.com_wallpaper.jpg',-1)

print(im)
print(im.shape)

for i in range(100):
    for j in range(im.shape[1]):
        im[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()