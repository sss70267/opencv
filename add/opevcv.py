import cv2
import numpy as np
#import matplotlib.pyplot as plt


img1 = cv2.imread('IMG_7805_resize.JPG')
img1_color = img1.copy()
img1 =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('person.jpg')
img2_shape = img2.shape

scale_percent =0.25
wigth = int(img2.shape[0]*scale_percent)
height = int(img2.shape[1]*scale_percent)

dim = (wigth,height)

img2_fg = cv2.resize(img2,dim,interpolation = cv2.INTER_AREA)
cv2.imwrite('./img2/person1.jpg',img2_fg)

img2_gray = cv2.cvtColor(img2_fg,cv2.COLOR_BGR2GRAY)
cv2.imwrite('./img2/person2.jpg',img2_gray)

h,w=img2_fg.shape[:2]

mask=np.zeros([h+2,w+2],np.uint8)

img3 = img2_fg.copy()

img4 = cv2.cvtColor(img3,cv2.COLOR_BGRA2RGB)
#plt.scatter(30,30,c='r')
#plt.imshow(img4)
#plt.grid()
#plt.show()

cv2.floodFill(img3,mask,(30,30),(255,255,255),
             (100,100,100),(50,50,50),cv2.FLOODFILL_FIXED_RANGE)

cv2.imwrite('./img2/person3.jpg',img3)

img3gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,mask2=cv2.threshold(img3gray,254,255,cv2.THRESH_BINARY)
cv2.imwrite('./img2/person4.jpg',mask2)

rows,cols,channels=img3.shape

x=100
y=150

roi=img1_color[y:y+rows,x:x+cols]
img1_bg=cv2.bitwise_and(roi,roi,mask=mask2)
cv2.imwrite('./img2/person5.jpg',img1_bg)

mask_inv=cv2.bitwise_not(mask2)
#cv2.imwrite('./img/person7.jpg',mask_inv)
img2_fg=cv2.bitwise_and(img3,img3,mask=mask_inv)
cv2.imwrite('./img2/person6.jpg',img2_fg)

dst=cv2.add(img1_bg,img2_fg)
img1_color[y:y+rows,x:x+cols]=dst
cv2.imwrite('./img2/person7.jpg',img1_color)