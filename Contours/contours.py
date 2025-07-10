import cv2
import numpy as np

image = cv2.imread('coins2.png')
print(image.shape) #(448, 599, 3)
r = 450/image.shape[0] #1.0044642857142858
print(r)
dim = (int(image.shape[1]*r),450)#(601, 450)
print(dim)


resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
gray= cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imwrite('coins2_1.png',gray)


blurred = cv2.GaussianBlur(gray,(11,11),0)
cv2.imwrite('coins2_blurred.png',blurred)


edged = cv2.Canny(blurred,30,150)
cv2.imwrite('coins2_edged.png',edged)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
close = cv2.morphologyEx(edged,cv2.MORPH_CLOSE,kernel)
cv2.imwrite('close.png',close)


contours,hierachy = cv2.findContours(close.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print('硬幣數量',len(contours))
#print('contours:',contours)
#print('hirechy:',hierachy)


coins = resized.copy()
cv2.drawContours(coins,contours,-1,(0,255,0),2)    #畫輪廓
cv2.imwrite('findcontours.png',coins)


for (i,c) in enumerate(contours):
    (x,y,w,h) = cv2.boundingRect(c)
    print('coin #',str(i+1))
    coin = resized[y:y+h,x:x+w]
    mask = np.zeros(resized.shape[:2],dtype='uint8')
    try:
        ((centerX,centerY),adius) = cv2.minEnclosingCircle(c)
        cv2.circle(mask,(int(centerX),int(centerY)),int(adius),255,-1)
        cv2.imwrite('./coins/mask-' + str(i+1) + '.png',mask)
        print('邏輯計算')
        mask2 = mask[y:y + h, x:x + w]
        coins2 = cv2.bitwise_and(coin,coin,mask = mask2)
        cv2.imwrite('./coins/coins2A-' + str(i+1) + '.png',coins2)
    except:
        print('circle無法產生')


a=1
clone = resized.copy()
for c in contours:
    M = cv2.moments(c)
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])
    cv2.circle(clone,(cX,cY),10,(1,255，254),-1)
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c,True)
    print(str(a)+'面積為:',area)
    print(str(a)+'周長為:',perimeter)
    a+=1
cv2.imwrite('clone.png',clone)
