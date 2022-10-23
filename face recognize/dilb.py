import  cv2,dlib
from  imutils import  face_utils
detect=dlib.get_frontal_face_detector()
predictoer=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def detect_Face_landmarks(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect(gray, 1)  # 偵測後找出臉部
    for face in faces:
        shape = predictoer(gray,face)
        shape = face_utils.shape_to_np(shape)
        x,y,w,h = face_utils.rect_to_bb(face)
        for (x,y) in shape:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
        cv2.imshow('img2',img)
    print('找到:',len(faces),'個人')
    cv2.imwrite('face_landmarks.png',img)

try:
    filename=('./faces/5566.jpg')
    detect_Face_landmarks(filename)
    cv2.waitKey()
    cv2.destroyAllWindows()
except:
    print('輸入錯誤')

