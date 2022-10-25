import os
import face_recognition 
import time
import socket

print("Find info on someones face by providing a image")
print("would you like to start the tool")
print("1 start")
print("99 exit")
starttool = input("Your choice: ")

if starttool == "1":
    print("starting tool")
    time.sleep(1)
    #paths of jpgs
    print("what is the jpg you would like to compare your image too")
    knownimagejpg = input("what is the jpg that is what you want to compare too that is known: ")
    time.sleep(2)
    print("what is the jpg that is unknown")
    unknownimagejpg = input("the unkown jpg that you want to compare to known: ")
    
    #load image jpgs 
    known_image = face_recognition.load_image_file(knownimagejpg)
    unknown_image = face_recognition.load_image_file(unknownimagejpg)

    #get face jpg encodings of each image
    try:
        person_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()
    
    known_faces = [
        person_encoding
    ]


    #[person_encoding]
    results = face_recognition.compare_faces(known_faces, unknown_encoding)



    
if starttool == "99":
    print("quiting")
    time.sleep(1)
    exit()

    
