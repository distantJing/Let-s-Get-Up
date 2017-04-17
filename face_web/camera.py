import picamera
import time
def capture_pic():
    # init
    filename = ""
    while True:
        camera = picamera.PiCamera()
        filename = time.strftime("%Y%m%d%H%M%S",time.localtime())+'.jpg'

        camera.capture(filename)
        classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
        frame = cv2.imread(filename)
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # 转为灰度图象
        faceRects = classifier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:
            break
    return filename

