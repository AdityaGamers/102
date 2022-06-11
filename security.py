from tracemalloc import take_snapshot
import cv2
import time
import random
import dropbox


startTime=time.time()
def takepicture():
    x=random.randint(0,100)
    cam=cv2.VideoCapture(0)
    result=True
    while result:
        ret,frame=cam.read()
        imageName="image"+str(x)+".jpg"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    cam.release()
    cv2.destroyAllWindows()

def uploadFile(imgName):
    file=imgName
    source=file
    destination="/security2/"+(imgName)
    dbx=dropbox.Dropbox("sl.BJVt6-5RXfUYoFxqym6mtO5_fMw9oc0OsSUbEQ1lc1dzh87Xg3AHd2g72OxLIxKkVkvdY7PUHU7hRzKKfE-IzNFKevcbWgFyCZgYJgyUfcAAAlaSrVcQpdH2JElfr8bdpZ-jg4OfAsE")
    with open(source,"rb")as img:
        dbx.files_upload(img.read(),destination,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while True:
        if((time.time()-startTime)>=30):
            img=takepicture()
            uploadFile(img)
main()
