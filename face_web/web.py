#coding=utf8
import requests,mimetypes,json,os,time
# from camera import capture_pic
import cv2
from weather import fetchWeather
# 这里填写你的应用的API Key与API Secret
API_KEY = 'CE_sha6AOEyahdZRn9sXwNq9uKEz8u0x'
API_SECRET = 'mnJrL83DFO3ikRHCVeuEld8SGOTuxGjJ'

# 目前的API网址是这个，你可以在API文档里找到这些
BASE_URL = 'https://api-cn.faceplusplus.com/facepp/v3'
BASE_PARAMS = {
    'api_key': API_KEY,
    'api_secret': API_SECRET, }

def upload_img(fileDir, oneface = True):
    url = '%s/detect?api_key=%s&api_secret=%s&attribute=none'%(
            BASE_URL, API_KEY, API_SECRET)
    if oneface: url += '&mode=oneface'
    files = {'image_file': (os.path.basename(fileDir), open(fileDir, 'rb'),
            mimetypes.guess_type(fileDir)[0]), }
    r = requests.post(url, files = files)
    faces = r.json().get('faces')
    if faces is None:
        return 
        None
    else:
        return faces[0]['face_token']

def compare(faceId1, faceId2):
    url = '%s/compare'%BASE_URL
    url = '%s/compare?api_key=%s&api_secret=%s&attribute=none'%(
            BASE_URL, API_KEY, API_SECRET)
    params = {}
    params['face_token1'] = faceId1
    params['face_token2'] = faceId2
    r = requests.post(url, data = params)
    return r.json()['confidence']

if __name__ == '__main__':
    yangId = upload_img('yang.jpg')
    wuId = upload_img('wu.jpg')
    heId = upload_img('he.jpg')
    confidence = {}
    print("taking picture now.")
    # pic = capture_pic()
    pic = "test1.jpg"
    
    faceId1 = upload_img(pic)
    # faceId1 = upload_img('test4.jpg')
    confidence['yang'] = compare(faceId1,yangId)
    confidence['wu'] = compare(faceId1,heId)
    confidence['he'] = compare(faceId1,wuId)
    flag = False
    for key, val in confidence.items():
        print(key,val)
        if val > 80:
            print(key + " is checked.")
            weather, temp = fetchWeather("成都")
            print("今天的天气是%s, 现在的温度是%s摄氏度."%(weather,temp))
            flag = True
            break
    if flag == False:
        print("nobody is checked. please check again.")


def test(filename):
    classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    frame = cv2.imread(filename)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # 转为灰度图象
    faceRects = classifier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
    faceRects = classifier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
    if len(faceRects) > 0:
        return True
    else :
        return False