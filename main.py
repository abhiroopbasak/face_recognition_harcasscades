import cv2
import sys
print(“Enter the path of the image”)
imagePath = input()
cascPath = “haarcascade_frontalface_default.xml”
faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
gray,
scaleFactor=1.1,
minNeighbors=5,
minSize=(1,1),
flags = cv2.CASCADE_SCALE_IMAGE
)
print(“{0} faces detectd!”.format(len(faces)))
for (x, y, w, h) in faces:
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow(“Faces Detected”, image)
cv2.waitKey(0)
