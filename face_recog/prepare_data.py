import numpy as np
import cv2
import os
import sys
import traceback

train_size = 10
WIDTH = 112
HEIGHT = 92
PIC_FORMAT = '.png'

TRAINDATA_NAME = 'traindata'
TEMP = 'picture'

CLASS = 'haarcascade_frontalface_alt2.xml'
CLASS1 = 'haarcascade_frontalface_default.xml'
KEY_VALUE = 'key-value.json'

def add_new_key_value(key, value):
	path = os.path.abspath('.')
	src = os.path.join(path,KEY_VALUE)
	file = open(src)
	js = json.load(file)
	file.close()
	js[key] = value
	file = open(src,'w')
	json.dump(js,file)
	file.close()

# creat the csv file 
# root_dir = traindata, log_name = train.txt
def creat_csv(root_dir,log_name):
	log_dir = os.path.join(root_dir,log_name) 
	fo = open(log_dir,"a") 
	files = os.listdir(root_dir)
	for file in files:
		if os.path.isdir(os.path.join(root_dir,file)):
			person_dir = os.path.join(root_dir,file) # /2
			if(os.path.isdir(person_dir)):
				pictures = os.listdir(person_dir)
				for pic in pictures:
					pic_dir = os.path.join(person_dir,pic)
					fo.write(pic_dir+';'+file+'\n')
			else:
				continue
	fo.close()


# save a picture
def save_pic(pic_path, pic_name, img):
	pic_dir = os.path.join(pic_path,pic_name)
	cv2.imwrite(pic_dir,img)

# take a picture when put a 's', esc is to exit
# pic_path = C:\Users\ZhiJing\Desktop\face_recog\traindata\1
def pic_catch(camera_id, pic_path):
	if(os.path.isdir(pic_path)==False):
		os.mkdir(pic_path)

	window_name = 'let\'s take a picture'
	cv2.namedWindow(window_name)

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
			# pic_path = os.path.abspath('.') + '/picture/s'+ str(peo_id) + '/'
			pic_name = str(pic_num) + PIC_FORMAT
			save_pic(pic_path,pic_name,frame)
			# cv2.imwrite(pic_path+pic_name,frame)

# src_path = C:\Users\ZhiJing\Desktop\face_recog\picture\s43
# dst_path = C:\Users\ZhiJing\Desktop\face_recog\traindata\1
def face(src_path, dst_path):
	if(os.path.isdir(src_path)==False):
		print("src_path is not exsist\n")
		return
	if(os.path.isdir(dst_path)==False):
		os.mkdir(dst_path)	
	face_cascade = cv2.CascadeClassifier(CLASS)
	# src_path = os.path.abspath('.') + '/picture/s'+ str(peo_id) + '/'
	# tar_path = os.path.abspath('.') + '/data/s'+ str(peo_id) + '/'
	imgs = os.listdir(src_path)
	for pic_name in imgs:
		src = os.path.join(src_path,pic_name)
		img = cv2.imread(src)
		# print(img)
		try:
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		except Exception as e:
			traceback.print_exc()
			continue
		faces = face_cascade.detectMultiScale(gray)
		if len(faces)>0:
			for faceRect in faces:
				x,y,w,h = faceRect
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)  
				roi_gray = gray[y:y+h,x:x+w]  
				roi_color = img[y:y+h,x:x+w]
		img_face = cv2.resize(roi_gray, (HEIGHT, WIDTH))
		save_pic(dst_path,pic_name,img_face)
		# cv2.imwrite(tar_path+pic_name,img_face)
		print(len(img_face))


# creat_csv('C:/Users/ZhiJing/Desktop/face_recog/traindata','train.txt')

if __name__ == '__main__':
	if sys.argv[1] == 'pic_catch':
		camera_id = 0
		base_path = os.path.join(os.path.abspath('.'),TEMP)
		fo = open(os.path.join(base_path,'log.txt'))
		peo_id = int(fo.readline())
		fo.close()
		pic_path = os.path.join(base_path,str(peo_id))
		pic_catch(camera_id, pic_path)
		# pic_path = C:\Users\ZhiJing\Desktop\face_recog\picture\1
	elif sys.argv[1] == 'creat_csv':
		root_dir = os.path.join(os.path.abspath('.'),TRAINDATA_NAME)
		log_name = 'train.txt'
		creat_csv(root_dir,log_name)
	elif sys.argv[1] == 'face':
		base_path = os.path.abspath('.')
		src = '1'
		dst = '45'
		src_path = os.path.join(os.path.join(base_path,TEMP),src)
		dst_path = os.path.join(os.path.join(base_path,TRAINDATA_NAME),dst)
		print(src_path)
		print(dst_path)
		face(src_path, dst_path)

