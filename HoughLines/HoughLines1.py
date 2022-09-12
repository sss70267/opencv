import cv2
import  numpy as np
img=cv2.imread('Lanes4.jpg')
house=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(house,100,250)
cv2.imwrite('3edges.png',edges)
#lines=cv2.HoughLines(edges,1,np.pi/180,200)
lines=cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength=5,maxLineGap=10)
print(np.shape(lines))
print(lines)
print('-'*70)
try:
    for line in lines:
        print('產生座標空間座標')
        x1,y1,x2,y2=line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255),3)
    cv2.imwrite('3edges1.png', img)
except:
    print('沒有直線')


