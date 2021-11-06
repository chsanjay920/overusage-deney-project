import cv2
import uuid
import numpy as np
from face_recognition import *

class cap(object):
    def __init__(self, *args):
        super(cap, self).__init__(*args)
        self.face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
    
    def face_extractor(self,img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]
        
        return cropped_face
    
    def GetUserImage(self):
        cap = cv2.VideoCapture(0)
        res,frame = cap.read()
        if self.face_extractor(frame) is not None:
            face = cv2.resize(self.face_extractor(frame), (200, 200))
            file_name_path = './faces/'+str(uuid.uuid4().hex)[:12] + '.jpg'
            cv2.imwrite(file_name_path,face)
        else:
            self.GetUserImage()
            
        cap.release()
        cv2.destroyAllWindows()