from urllib import request, parse
import json
import requests

# getValue地址
get_value_path = "http://127.0.0.1:11000/getVal"
# getValue地址
set_value_path = "http://127.0.0.1:11000/setVal"

# 负载均衡
class LBMger(object):
    # 服务器列表
    ser_list = None

    def __init__(self):
        self.ser_list = []

    # 添加一个新的服务器
    def add_ser(self, ser_data):
        tmp_data = {
            "ip" : ser_data["ip"],
            "port" : ser_data["ip"]
        }
        self.ser_list.append(ser_data)

    # 发送get请求
    def send_get(self, key):
        send_str = "%s?key=%s"%(get_value_path, key)
        ret = request.Request(send_str)
        response = request.urlopen(ret)
        return response.read().decode('utf-8')
    
    # 发送post请求
    def send_post(self, key, val):
        headers = {'content-type':'application/json'}
        data = {
            'key': key,
            'val': val
        }
        response = requests.post(set_value_path, data=json.dumps(data),headers=headers)
        return response.text