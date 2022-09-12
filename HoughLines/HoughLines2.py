import  cv2
import  numpy as np
def line_detection(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #若有需要可以再加入型態調整
    edge=cv2.Canny(gray,50,150,apertureSize=3)
    lines=cv2.HoughLines(edge,1,np.pi/180,300)
    for line in lines:
        rho,theta=line[0]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        x1=int(x0+1000*(-b)) #1000代表長度
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b)) #1000代表長度
        y2=int(y0-1000*(a))
        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.imwrite('./lines/image-lines'+str(line)+'.png',image)
def line_detect_possible(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,50,150,apertureSize=3)
    lines=cv2.HoughLinesP(edge,1,np.pi/180,75,minLineLength=70,maxLineGap=5)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imwrite('./lines/image-lines-p'+str(line)+'.png', image)
src=cv2.imread('lee.jpg')
src=cv2.GaussianBlur(src,(5,5),5)
line_detection(src)
line_detect_possible(src)
