from retinaface import RetinaFace

import cv2

def face_detect(imagePath):
    
    img = cv2.imread(imagePath)

    img_1 = cv2.resize(img, (1000,700))

    gray = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
    faces = RetinaFace.detect_faces(img_1, threshold = 0.1)

    print('Number of detected faces:', len(faces))

    print(faces)

    face = []
    grays=[]
    for i, key in enumerate(faces):
        
        identity = faces[key]
         
        facial_area = identity["facial_area"]
        
        face1 = [2,3,4,5]
        cv2.rectangle(img_1, (facial_area[2], facial_area[3])
           , (facial_area[0], facial_area[1]), (0, 255, 0), 2)
        
        face1.append(facial_area[2])
        face1.append(facial_area[1])
        face1.append(facial_area[3] - facial_area[1])
        face1.append(facial_area[2] - facial_area[0])
        
        face.append(face1)

    #cv2.imshow("image", img_1)
    cv2.waitKey(1)
    for i in faces :
        identity = faces[i]
        facial_area = identity["facial_area"]
        grays.append(gray[facial_area[1]:facial_area[3],facial_area[0]:facial_area[2]])
        
    return grays,face, len(face)
  