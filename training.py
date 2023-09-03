# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:56:29 2023

@author: Lenov
"""

import cv2, os, sys
import numpy as np
import face_detect as face_detect

def training_data(data_folder):
    dirs = os.listdir(data_folder)
    faces = []
    labels = []
    for dir_name in dirs:
      
        #label = int(dir_name.replace("s", ""))
        label=os.path.basename(os.path.dirname(dir_name)).replace(" ","-")
        subject_dir = data_folder + "/" + dir_name
        subject_images_names = os.listdir(subject_dir)
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;
            image_path = subject_dir + "/" + image_name
            face, rect, length = face_detect.face_detect(image_path)
            if face is not None:
                faces.append(face[0])
                labels.append(label)
                
    return faces, labels