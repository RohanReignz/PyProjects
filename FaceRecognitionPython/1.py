import cv2
import numpy as np

capture = cv2.VideoCapture(0)
#Saving
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
	ret, img = capture.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#	out.write(img)
	cv2.imshow('Webcam',img)
	cv2.imshow('Gray', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

capture.release()
#out.release()
cv2.destroyAllWindows()