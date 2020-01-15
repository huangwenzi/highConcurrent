from urllib import request, parse
import json
import requests

# 负载均衡地址
# 电脑地址 http://127.0.0.1:11000
# 域名地址 http://thiswen.cn:11000
# 数据服务器地址
# 电脑地址 http://127.0.0.1:10001
# 域名地址 http://thiswen.cn:10001

# getValue地址
get_value_path = "http://127.0.0.1:11000/getVal"
# getValue地址
set_value_path = "http://127.0.0.1:11000/setVal"

# 模拟客户端管理器
class ClientMgr(object):
    def __init__(self, *args):
        pass
        
    # 发送get请求
    def send_get(self, key):
        send_str = "%s?key=%s"%(get_value_path, key)
        ret = request.Request(send_str)
        response = request.urlopen(ret)
        return response.read().decode('utf-8')
    
    # 发送post请求
    def send_set(self, key, val):
        headers = {'content-type':'application/json'}
        data = {
            'key': key,
            'val': val
        }
        response = requests.post(set_value_path, data=json.dumps(data),headers=headers)
        return response.text

