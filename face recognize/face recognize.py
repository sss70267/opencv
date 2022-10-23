import cv2
from PIL import  Image
casc_path = './cascade_files/haarcascade_frontalface_default.xml'
Face_Cascade = cv2.CascadeClassifier(casc_path)
image = cv2.imread('./faces/group_photos.jpg')
pil_image = Image.open('./faces/group_photos.jpg')
faces = Face_Cascade.detectMultiScale(image,
                                      scaleFactor=1.1,
                                      minNeighbors=4,
                                      minSize=(3,3),
                                      maxSize=(57,57))
count = 1
for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    filename = './media/face' +str(count) + '.jpg'
    image_crop = pil_image.crop((x,y,x+w,y+h))
    image_crop.save(filename)
    count += 1

cv2.putText(image,'Find'+str(len(faces))+'faces',(0,image.shape[0]),
            cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),2)

cv2.imshow('facedetect',image)
cv2.imwrite('face_recognition1.jpg',image)


cv2.waitKey(1000)
cv2.destroyAllWindows()