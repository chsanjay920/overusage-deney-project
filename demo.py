import face_recognition
import glob

# known_image = face_recognition.load_image_file("./faces/d6b24731dcaa.jpg")
# unknown_image = face_recognition.load_image_file("./faces/3891e9a8d6e2.jpeg")

# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# for img in glob.iglob('./known_faces/*.jpg',recursive=True):
#     known_image = face_recognition.load_image_file(img)
#     known_imgEncoading = face_recognition.face_encodings(known_image)[0]
#     result = face_recognition.compare_faces([known_imgEncoading],unknown_encoding)
#     print(result)

for img in glob.iglob('./known_faces/*.jpg',recursive=True):
    print(img)
    # known_image = face_recognition.load_image_file(img)
    # known_imgEncoading = face_recognition.face_encodings(known_image)[0]
    # result = face_recognition.compare_faces([known_imgEncoading],)
    # if result[0]:
    #     print("person found")
    #     break
    # else:
    #     print("unknown person ")
