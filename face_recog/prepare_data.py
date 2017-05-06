import numpy as np
import cv2
import os
import sys

train_size = 10
pic_format = '.png'
# creat the csv file 
# python *.py creat_csv peo_num
# peo_num is the total number of dataset
def creat_csv(peo_num):
	path = os.path.abspath('.')
	fo = open(path + '/data/' +"at.txt", "a")
	for i in range(41, peo_num+1):
		for j in range (1, train_size+1):
			csv = path + '/data/s' + str(i) + '/' + str(j) + pic_format+';' + str(i) + '\n'
			print(csv)
			fo.write(csv)
	fo.close()


# take a picture when put a 's', esc is to exit
# python *.py pic_catch peo_id
# peo_id is the current number of this data set
def pic_catch(window_name, camera_id, peo_id):
	window_name = 'let\'s take a picture'
	cv2.namedWindow(window_name)
	os.mkdir('test/s'+str(peo_id))

	cap = cv2.VideoCapture(camera_id)
	pic_num = 0

	while cap.isOpened:
		ok, frame = cap.read()
		if not ok:
			break
		cv2.imshow(window_name, frame)
		k = cv2.waitKey(10)
		if k == 27:         # wait for ESC key to exit
			cap.release()
			cv2.destroyAllWindows()
		elif k == ord('s'): # wait for 's' key to save and exit
			pic_num = pic_num + 1
			pic_path = os.path.abspath('.') + '/test/s'+ str(peo_id) + '/'
			pic_name = str(pic_num) + pic_format
			cv2.imwrite(pic_path+pic_name,frame)

# get the face of peo_id
def face(peo_id):
	width = 112
	height = 92
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	pic_path = os.path.abspath('.') + '/data/s'+ str(peo_id) + '/'
	for i in range (1, train_size+1):
		pic_name = str(i) + pic_format
		img = cv2.imread(pic_path+pic_name)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray)
		if len(faces)>0:
			for faceRect in faces:
				x,y,w,h = faceRect
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)  
				roi_gray = gray[y:y+h,x:x+w]  
				roi_color = img[y:y+h,x:x+w]
		img_face = cv2.resize(roi_gray, (height, width))
		cv2.imwrite(pic_path+pic_name,img_face)
		print(len(img_face))

# face(44)

if __name__ == '__main__':
	if sys.argv[1] == 'pic_catch':
		window_name = 'let\'s take a picture'
		camera_id = 0
		peo_id = 1
		pic_catch(window_name, camera_id, peo_id)
	elif sys.argv[1] == 'creat_csv':
		peo_num = int(sys.argv[2])
		creat_csv(peo_num)

