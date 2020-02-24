import cv2
import numpy as np

face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Takes in the xml
eye_cas = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture('unbox.mp4') #Captures video from webcam

while True:	#loops continuously and so takes in every frame
	rat, img = cap.read()	#reads the images
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#changes to grayscale
	faces = face_cas.detectMultiScale(gray, 1.3, 5)	#detects the face by matching certain patterns of arrays
	for (x,y,w,h) in faces:		#start to draw a rectangle
		o =cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)	#draw a rectangle on to the img, start x,y and increase to  w,h, colored Red (BGR) and width is 2px
		if o.all() != None:
			cv2.putText(img, 'Face Detected!', (x-3, y-3), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 1, cv2.LINE_AA)
		else:
			break 
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cas.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)	#draws rectangle for eyes
	cv2.imshow('img', img)	#shows the img in a window called 'img'
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
	#Stops reading from the webcam
cv2.destroyAllWindows()	#Destroys all other windows after the condition is broken