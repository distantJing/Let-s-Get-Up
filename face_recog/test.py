import cv2
import os
import re
import traceback
import numpy as np

SIZE = 30912
WIDTH = 112
HEIGHT = 92

CLASS = 'haarcascade_frontalface_alt2.xml'
CLASS1 = 'haarcascade_frontalface_default.xml'

# img = cv2.imread('C:/Users/ZhiJing/Desktop/face_recog/data/s1/1.png')
model1 = cv2.face.createEigenFaceRecognizer()
model2 = cv2.face.createFisherFaceRecognizer()

# model1.load('model1')
model2.load('model2')

# for i in range(1,27):
# 	src = cv2.imread('C:/Users/ZhiJing/Desktop/face_recog/data/s44/'+str(i)+'.png')
# 	src = np.array(src).reshape(1,SIZE)
# 	a = model2.predict(src)
# 	print(str(i)+" "+str(a[0])+" "+str(a[1]))

window_name = 'who am i?'
camera_id = 0
cv2.namedWindow(window_name)
cap = cv2.VideoCapture(camera_id)
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(CLASS)

def predict(frame):
	faces = face_cascade.detectMultiScale(frame)
	print('the face number is ' + str(len(faces)))
	if len(faces)>0:
		for faceRect in faces:
			x,y,w,h = faceRect
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,8,0)
			img = frame[y:y+h,x:x+w]
			img = cv2.resize(img, (HEIGHT, WIDTH))
			# cv2.imshow("img",img)
			try:
				img = np.array(img).reshape(1,SIZE)
			except Exception as e:
				traceback.print_exc()
				continue
			face_info = model2.predict(img)
			print(face_info)
			cv2.putText(frame,str(face_info[0]), (x + 30, y + 30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
		cv2.imshow("who am i?", frame)

while cap.isOpened:
		ok, frame = cap.read()
		if not ok:
			break
		# cv2.imshow(window_name, frame)
		k = cv2.waitKey(10)
		if k == 27:         # wait for ESC key to exit
			cap.release()
			cv2.destroyAllWindows()
		else:
			predict(frame)
			# print('lalala')

