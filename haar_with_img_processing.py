import cv2

# read the input image
img = cv2.imread('test/7.jpg')

# increases brightness 

alpha = 1.5 # Contrast control
beta = 14 # Brightness control

img_b = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
# image crop 
img_c = img_b[450:1000, 50:1100]

# image resize

img_1 = cv2.resize(img_c, (1000,700))
# convert to grayscale of each frames
gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)



# read the haarcascade to detect the faces in an image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detects faces in the input image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print('Number of detected faces:', len(faces))
print(faces)

# loop over all detected faces
if len(faces) > 0:
   for i, (x,y,w,h) in enumerate(faces):
       
      # To draw a rectangle in a face
      cv2.rectangle(img_1,(x,y),(x+w,y+h),(0,255,255),2)
      face = img_1[y:y+h, x:x+w]
      cv2.imshow(f"Cropped Face {i}", face)
      cv2.imwrite(f'face{i}.jpg', face)
      print(f"face{i}.jpg is saved")

# display the image with detected faces
cv2.imshow("image", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
