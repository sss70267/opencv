import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('25551961_1664797076917161_5287691592790831275_n.jpg')
print(img.shape) #(342,548,3)

mask = np.zeros(img.shape[:2],np.uint8)
print(mask.shape) #(342, 548)

bgdModel = np.zeros((1,65),np.float64)
fgbModel = np.zeros((1,65),np.float64)
print(bgdModel.shape,fgbModel.shape)  #(1, 65) (1, 65)


rect = (0,25,960,695) #(x1,x2,x3,x4) X1+x3 x2+x4選取範圍
np.savetxt('mask1.txt',mask,fmt='%1d')  ##

cv2.rectangle(img,rect,(0,0,255),2)
img2 = cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
plt.imshow(img2)
plt.show()

cv2.grabCut(img,mask,rect,bgdModel,fgbModel,15,cv2.GC_INIT_WITH_RECT)
cv2.imwrite('grabcut1.png',img)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
print(mask2.shape) #(342, 548)
np.savetxt('mask2.txt',mask2,fmt='%1d')

img3=img*mask2[:,:,np.newaxis]
print(img3.shape)
cv2.imwrite('grabute2.png',img3)