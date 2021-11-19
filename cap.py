import cv2
import uuid
import face_recognition
import numpy as np
from face_recognition import *
import glob
import json
import time

class cap(object):
    def __init__(self, *args):
        super(cap, self).__init__(*args)
        self.face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
        self.flag = 0
    
    def face_extractor(self,img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_face = img[y+3:y+h+3, x+3:x+w+3]
        return cropped_face

    def addUser(self,userid):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        users = {'name': userid, 'time': current_time}
        y = json.loads(users)

    def compareFaces(self):
        unknown_imgEncodeing = face_recognition.face_encodings(self.face)[0]
        for img in glob.iglob('./known_faces/*.jpg',recursive=True):
            known_image = face_recognition.load_image_file(img)
            try:
                print("=================pass =============")
                known_imgEncoading = face_recognition.face_encodings(known_image)[0]
                result = face_recognition.compare_faces([known_imgEncoading],unknown_imgEncodeing)
                if result[0]:
                    self.flag = 1
                    print("person found",str(img)[14:])
                    break
                else:
                    print("unknown person ",str(img)[14:])
            except:
                print("=================exception =============")
        if(self.flag == 0):
            userid = str(uuid.uuid4().hex)[:12]
            file_name_path = './known_faces/'+ userid+ '.jpg'
            cv2.imwrite(file_name_path,self.face)
            self.addUser(userid)
            

    def GetUserImage(self):
        cap = cv2.VideoCapture(0)
        res,frame = cap.read()
        if self.face_extractor(frame) is not None:
            self.face = cv2.resize(self.face_extractor(frame), (600, 600))
            file_name_path = './faces/'+str(uuid.uuid4().hex)[:12] + '.jpg'
            cv2.imwrite(file_name_path,self.face)
            cap.release()
            cv2.destroyAllWindows()
            self.compareFaces()
        else:
            self.GetUserImage()