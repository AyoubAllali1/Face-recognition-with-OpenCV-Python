import cv2 

vid = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    _,frame = vid.read()
    
    faces = classifier.detectMultiScale(frame)
    for face in faces:
        x,y,width,height = face
        cv2.rectangle(frame, (x,y), (x + width, y + height), (0,255,0), 2)

    cv2.imshow('face recognition',frame)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

