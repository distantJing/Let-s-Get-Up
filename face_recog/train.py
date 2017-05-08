import cv2
import os
import re
import numpy as np

SIZE = 30912
TRAINDATA_NAME = 'traindata'
TRAIN_LOG_NAEM = 'train.txt'

path = os.path.abspath('.')
# fo = open(path + '/data/' +"at.txt", 'r')
fo = open(os.path.join(path,TRAINDATA_NAME,TRAIN_LOG_NAEM),'r')
lines = fo.readlines()

imgs = []
labels = []

for line in lines:
	img_url, label = re.split(';', line)
	# print(line)
	img = cv2.imread(img_url)
	print(line)
	imgs.append(np.array(img).reshape(1,SIZE))
	labels.append(int(label))

# img = cv2.imread('C:/Users/ZhiJing/Desktop/face_recog/data/s1/1.png')
model1 = cv2.face.createEigenFaceRecognizer()
model2 = cv2.face.createFisherFaceRecognizer()
model3 = cv2.face.createLBPHFaceRecognizer()
model1.train(imgs, np.array(labels))
model2.train(imgs, np.array(labels))
# model3.train(imgs, np.array(labels))

model1.save('model1')
model2.save('model2')

# for i in range(1,6):
# 	src = cv2.imread('C:/Users/ZhiJing/Desktop/face_recog/traindata/45/'+str(i)+'.png')
# 	src = np.array(src).reshape(1,SIZE)
# 	a = model2.predict(src)
# 	print(a)

