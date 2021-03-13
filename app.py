import face_recognition
 
known_image = face_recognition.load_image_file("charmi1.jpeg") 
unknown_image = face_recognition.load_image_file("image.jpeg")
 
biden_encoding = face_recognition.face_encodings(known_image)[0] 
unknown_encoding = face_recognition.face_encodings(unknown_image)[0] 
 
result = face_recognition.compare_faces([biden_encoding], unknown_encoding) 

print(result)