from retinaface import RetinaFace
import cv2
import pickle
#from deepface import DeepFace


img_path = "dataset/DSC_1342.jpg"
img = cv2.imread(img_path)

img_1 = cv2.resize(img, (1000,700))

faces = RetinaFace.detect_faces(img_1, threshold = 0.1)
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer = cv2.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels={"person_name":1}
with open("labels.pickle",'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}
print('Number of detected faces:', len(faces))

print(faces)

gray=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
alpha = 1.5  # Contrast control
beta = 14  # Brightness control

for i, key in enumerate(faces):
    
    identity = faces[key]
     
    facial_area = identity["facial_area"]

    cv2.rectangle(img_1, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (0, 255, 0), 1)
    face_crop = img_1[facial_area[1]:facial_area[3], facial_area[0]:facial_area[2]]
    face=cv2.resize(face_crop,(120,120))

    img_p = cv2.convertScaleAbs(face, alpha=alpha, beta=beta)
    image = cv2.cvtColor(img_p, cv2.COLOR_BGR2GRAY)
    #clahe = cv2.createCLAHE(clipLimit=5)
    #final_img = clahe.apply(image)


    #image=cv2.imwrite(f'face{i}.jpg', img_p)
    id, conf = recognizer.predict(image)
    if conf >= 45 :
        print(id)
        print(labels[id])
        font=cv2.FONT_HERSHEY_SIMPLEX
        name=labels[id]
        color=(255,255,255)
        stroke=1
        cv2.putText(img_1,name,(facial_area[0],facial_area[1]),font,0.5,color,stroke)

    #cv2.imshow(f"Cropped Face {i}", final_img)
    cv2.imwrite(f'face{i}.jpg', image)
    #.......................
    print(f"face{i}.jpg is saved")
    #obj = DeepFace.verify("train/harsh/1.jpg", f"face{i}.jpg",enforce_detection=False, model_name='ArcFace', detector_backend='retinaface')
    #print(obj["verified"])

cv2.imshow("image", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()


