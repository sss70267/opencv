import face_recognition,cv2
input_movie = cv2.VideoCapture(input('輸入影片名稱:'))
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))#'計算影像長度
fourcc = cv2.VideoWriter_fourcc(*'XVID') #產生想要寫入的影片資訊
output_movie = cv2.VideoWriter('output.mp4',fourcc,24.00,(360,640))

#載入圖像
img1 = face_recognition.load_image_file(input('輸入圖片名曾稱:'))
try:
    img1_encoding = face_recognition.face_encodings(img1)[0]
except:
    print('無法進行編碼')
    quit()
known_faces = [img1_encoding]

face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while input_movie.isOpened():
    ret,frame = input_movie.read()
    frame_number += 1
    if not ret:
        break
    rgb_frame = frame[:,:,::-1]#bgr->rgb
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
    face_names = []

    for face_encoding in face_encodings:
        math = face_recognition.compare_faces(known_faces,face_encoding,tolerance=0.50)
        name = None
        if math[0]:
            name = 'Zheng'
        else:
            print('0')
        face_names.append(name)

    for (top,right,bottom,left),name in zip(face_locations,face_names):
        if not name:
            continue
        cv2.rectangle(frame,(left,top),
                      (right,bottom),(0,0,255),2)
        cv2.rectangle(frame, (left, bottom - 25),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    print('Writing frame:', frame_number, 'length:', length)
    output_movie.write(frame)