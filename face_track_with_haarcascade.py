import cv2

def fd(img):
    fc=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=fc.detectMultiScale(imggray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

def eyes(img):
    ev = cv2.CascadeClassifier("haarcascade_eye.xml")
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    evs = ev.detectMultiScale(imggray, 1.1, 4)

    for (x, y, w, h) in evs:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success,img=cap.read()
    fd(img )
    eyes(img)
    cv2.imshow("Video",img)
    if cv2.waitKey(1)  & 0xFF ==ord("q"):
        break