# Face-Recognition-From-Drone-Images 

## INTRODUCTION 

Face detection is a computer technology used to automatically detect human faces in
images or videos. It is an important step in many applications of computer vision, such
as face recognition, video surveillance, and human-computer interaction. The process
of face detection involves analyzing an image or video frame to determine the presence and location of faces. This is achieved by using algorithms and machine learning
techniques that can detect patterns of pixels that correspond to facial features, such as
the eyes, nose, and mouth. One common approach to face detection is the Viola-Jones
algorithm, which uses acombination of Haar-like features and a cascade classifier to
quickly identify faces in images. Other popular methods include deep learning-based
approaches, such as Convolutional Neural Networks (CNNs). Face detection has many
practical applications, such as in social media platforms that automatically tag faces in
photos, security systems that monitor public spaces for potential threats.
Face recognition is the process of identifying or verifying the identity of an individual
based on their facial features. This technology has become increasingly popular and
is now widely used in various applications, such as security systems, law enforcement,
and access control. The process of face recognition involves capturing an image or
video of a person’s face, and then using algorithms and machine learning techniques to
analyze and extract key features from the face, such as the distance between the eyes,
the shape of the jawline, and the contours of the nose and mouth. These features are
then compared with a database of known faces to determine the identity of the person.
There are two main types of face recognition: 1) verification, which is used to confirm
the identity of an individual, and 2) identification, which is used to match an unknown
face to a known individual.
Image processing is the use of mathematical and computational techniques to modify
or enhance digital images. These techniques can be used to improve the quality of
an image, extract useful information from it, or even create entirely new images from
existing ones. Image processing algorithms can be used for a variety of applications,
including image restoration, image compression, feature extraction, and image segmentation. 
For example, image restoration algorithms can be used to remove noise or blur
from an image, while image compression algorithms can reduce the size of an image
while retaining as much visual information as possible.

## OBJECTIVE 

• To recognize person from the long distance and large angle of elevation from the
drone. <br>
• To identify and develop a machine learning model that can accurately identify a
person from images or videos captured from a drone. <br>
• To obtain master technology for surveillance with very less human intervention. <br>

## PROBLEM IDENTIFICATION

While face recognition technology can be very effective in small-scale applications,
such as unlocking a smartphone or verifying a passport, it becomes more difficult to
scale the technology for larger populations or more complex scenarios. It has improved
significantly in recent years, it is still not perfect. Errors can occur due to poor lighting,
facial occlusions, or other factors. This can be particularly problematic in high-stakes
contexts such as law enforcement or national security. Face recognition technology can
exhibit bias, particularly if the algorithms are trained on biased datasets or if the technology is not designed to work with diverse populations. This can result in inaccurate
or discriminatory results, particularly for certain demographic groups.
Below are some problematic factors that affects the face detection and recognition for
images captured from a higher angle of elevation.

![image](https://github.com/PriteshPatel4739/Face-Recognition-From-Drone-Images/assets/69390119/ec01366f-2c89-4ae0-8279-3c58812b8583) 
Figure 1.1  Low Light Conditions 
![image](https://github.com/PriteshPatel4739/Face-Recognition-From-Drone-Images/assets/69390119/a8bcc234-7b03-4442-9150-f0fb884b4581)
Figure 1.2 Change in Angle of Elevation


## FLOW OF THE SYSTEM 

![image](https://github.com/PriteshPatel4739/Face-Recognition-From-Drone-Images/assets/69390119/79589073-6d0b-4f63-bae1-a7b41010dcf0)

### Data Base 

Firstly we found one data set from zapaniz university reasearch paper but it has not more variation in distance and height as well as there were at most 3 people in one frame but we want at least 7 people in one frame and photoes taken from higher height and distance so we have created our own dataset for this journey.

### Face Detection 

Initially we used 
### Haar cascade 
method for face detection but in result we are not getting more accuracy and also rate of false positive is also high then we thought that whay can't we apply some image pre-procesing on that image , after that we could remove false positive but detected face were not increasing . then we decided to change the algorithm of face detection. so after that we used 
### Retina Face 
algorithm for face detection and we got more accurate results.

### Image pre-processing 

![image](https://github.com/PriteshPatel4739/Face-Recognition-From-Drone-Images/assets/69390119/b52fe0d4-2773-4b39-8958-d7fc4f8ee531)





