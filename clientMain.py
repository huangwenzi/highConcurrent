import urllib
from urllib import request, parse
import json
import requests

# 模拟客户端请求

# 电脑地址 http://127.0.0.1:10001
# 域名地址 http://thiswen.cn:10001

# get
ret = request.Request('http://127.0.0.1:10001/getVal?key=a')
response = request.urlopen(ret)
print(response.read().decode('utf-8'))

# post
headers = {'content-type':'application/json'}
url="http://127.0.0.1:10001/setVal"  
data = {
    'key': 'a',
    'val': '1'
}
response = requests.post(url, data=json.dumps(data),headers=headers)
print(response.text)