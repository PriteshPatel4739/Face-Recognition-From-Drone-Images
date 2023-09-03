# import required libraries
import cv2

# Reading the Image
img = cv2.imread('test/7.jpg')


alpha = 1.5 # Contrast control
beta = 14 # Brightness control

# call convertScaleAbs function
img_b = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
img_c = img_b[450:1000, 50:1100]

img_1 = cv2.resize(img_c, (1000,700))

# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# detect humans in input image
(humans, _) = hog.detectMultiScale(img_1, winStride=(10, 10),
padding=(32, 32), scale=1.1)

# getting no. of human detected
print('Human Detected : ', len(humans))

# loop over all detected humans
for i, (x, y, w, h) in enumerate(humans):
   pad_w, pad_h = int(0.15 * w), int(0.01 * h)
   cv2.rectangle(img_1, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 1)
   
   hu = img_1[y+pad_h:y + h - pad_h, x+pad_w:x + w-pad_w]
   
   
   cv2.imshow(f"human{i}", hu)
   #cv2.imwrite(f"human{i}", hu)
   
   
   gray = cv2.cvtColor(hu, cv2.COLOR_BGR2GRAY)



   # read the haarcascade to detect the faces in an image
   face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

   # detects faces in the input image
   faces = face_cascade.detectMultiScale(gray, 1.1, 4)
   
   for i, (a,b,c,d) in enumerate(faces):
       
      # To draw a rectangle in a face
      cv2.rectangle(hu,(a,b),(a+c,b+d),(0,255,255),2)
   
 
   
   
   
   
 
# display the output image
cv2.imshow("Image", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()


