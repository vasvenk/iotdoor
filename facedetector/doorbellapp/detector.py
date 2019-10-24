import face_recognition
from os import listdir
from os.path import isfile, join

allPeople = ["Anoushka", "Tyler", "Andy", "Vas"]
baseLoc = "/home/nvidia/innopic/"


def detectFace(fileLoc):
    targetPic = face_recognition.load_image_file(fileLoc)
    target = face_recognition.face_encodings(targetPic)[0]

    personVote = {}
    for person in allPeople:
        personVote[person] = 0

    for person in allPeople:

        personLoc = baseLoc + person + "/"

        allPics = [personLoc + f for f in listdir(personLoc) if isfile(join(personLoc, f)) and ".jpg" in f]

        for pic in allPics:
            refPic = face_recognition.load_image_file(pic)
            refEncoded = face_recognition.face_encodings(refPic)
            if len(refEncoded) == 0:
                continue
            refEncoded = refEncoded[0]

            results = face_recognition.compare_faces([target], refEncoded)

            if results[0] == True:
                print("This is: " + max(allPeople, key=lambda x: personVote[x]) + "!!\n")
                return max(allPeople, key=lambda x: personVote[x])
                
    print("This is: " + max(allPeople, key=lambda x: personVote[x]) + "!!\n")
    return max(allPeople, key=lambda x: personVote[x])
    

    