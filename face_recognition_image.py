import cv2 

image = cv2.imread("your_image.png")

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = classifier.detectMultiScale(image)

for face in faces:
    x,y,width,height = face

    cv2.rectangle(image, (x,y), (x + width, y + height), (0,255,0), 1)

cv2.imshow('face recognition',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
