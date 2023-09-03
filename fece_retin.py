from retinaface import RetinaFace

import cv2


img_path = "dataset/DSC_1337.jpg"
img = cv2.imread(img_path)

img_1 = cv2.resize(img, (1000,700))

faces = RetinaFace.detect_faces(img_1, threshold = 0.1)

print('Number of detected faces:', len(faces))

print(faces)



for i , key in enumerate(faces):
    
    identity = faces[key]
     
    facial_area = identity["facial_area"]


    cv2.rectangle(img_1, (facial_area[2], facial_area[3])
       , (facial_area[0], facial_area[1]), (0, 255, 0), 1)
    
    face = img_1[facial_area[1]:facial_area[3],facial_area[0]:facial_area[2]]
    cv2.imshow(f"Cropped Face {i}", face)
    cv2.imwrite(f'face{i}.jpg', face)
    print(f"face{i}.jpg is saved")
    

cv2.imshow("image", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()


