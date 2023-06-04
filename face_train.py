import os
import cv2 as cv
import numpy as np

people = ["billgates","elonmusk","markzuck","ratantata"]
DIR = r"C:\Users\divyam\Documents\ComputerVision\train"
haar_cascade = cv.CascadeClassifier("haar_face.xml")    # Instantiating HaarCascade Classifier

features = []
labels =[]

# Creting function to get features and labels of the images -->
def create_train():
    for i in people:
        path = os.path.join(DIR, i)   #grabbing the path of every folder in train folder.
        label = people.index(i)    # [0,1,2,3]

        for imgs in os.listdir(path):
            img_path = os.path.join(path, imgs)

            img_array = cv.imread(img_path)
            gray_img = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors =4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray_img[y:y+h,x:x+w]      # faces_region of interest -->Grab/Crop the face from the image
                features.append(faces_roi)
                labels.append(label)

create_train()
# Converting list of features and labels to numpy array -->
features = np.array(features,dtype="object")   
labels = np.array(labels)

print(f"length of the features: {len(features)}")
print(f"length of the labels: {len(labels)}")

#  Using the above features and labels to train face recogonizer -->
face_recognizer = cv.face.LBPHFaceRecognizer_create()   # OpenCv's Built-In face-recognizer
face_recognizer.train(features,labels)           # Training the model on the features and labels.


face_recognizer.save("face_trained.yml")    # Saving teh trained model in yml format
np.save("features.npy",features)    
np.save("labels.npy",labels)
