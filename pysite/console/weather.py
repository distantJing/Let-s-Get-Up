import json
import sys
import requests

def fetchWeather(location):
    API = "https://api.seniverse.com/v3/weather/now.json"
    KEY = "yqr9cezs9faqguf9"
    ID = "U652F7D19A"
    # 中文简体
    LANGUAGE = "zh-Hans"
    # 单位 当参数为c时，温度c、风速km/h、能见度km、气压mb
    UNIT = "c"
    result = requests.get(API, params = {
        'key': KEY,
        'location' : location,
        'language': LANGUAGE,
        'unit' : UNIT
    }, timeout = 1)
    ret = result.json()['results'][0]['now']
    return ret['text'], ret['temperature']

