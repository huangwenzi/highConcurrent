from urllib import request, parse
import json
import requests

# getValue地址
get_value_path = "http://%s:%d/getVal"
# setValue地址
set_value_path = "http://%s:%d/setVal"

# 负载均衡
class LBMger(object):
    # 服务器列表
    svr_list = None
    # 当前执行命令的服务器idx
    now_idx = 0

    def __init__(self):
        self.svr_list = []

    # 添加一个新的服务器
    def add_svr(self, svr_data):
        tmp_data = {
            "ip" : svr_data["ip"],
            "port" : svr_data["port"]
        }
        self.svr_list.append(tmp_data)
        print("add_svr")
        print(self.svr_list)

    # 发送get请求
    def send_get(self, key):
        try:
            svr_info = self.get_now_svr_info()
            if not svr_info:
                return "没有工作中的服务器"
            # 发送
            send_str = (get_value_path + "?key=%s")%(svr_info["ip"], svr_info["port"], key)
            print("send_str:%s"%(send_str))
            ret = request.Request(send_str)
            print(ret)
            response = request.urlopen(ret)
            # 服务器顺序加一
            self.svr_now_idx_add()
            return response.read().decode('utf-8')
        except :
            # 失败删除当前连接的服务器,继续调用该函数
            self.remove_now_svr_info()
            return self.send_get(key)
    # 发送post请求
    def send_post(self, key, val):
        try:
            svr_info = self.get_now_svr_info()
            if not svr_info:
                return "没有工作中的服务器"
            # 发送
            send_path = set_value_path%(svr_info["ip"], svr_info["port"])
            print("send_path:%s"%(send_path))
            headers = {'content-type':'application/json'}
            data = {
                'key': key,
                'val': val
            }
            response = requests.post(send_path, data=json.dumps(data),headers=headers)
            # 服务器顺序加一
            self.svr_now_idx_add()
            return response.text
        except :
            # 失败删除当前连接的服务器,继续调用该函数
            self.remove_now_svr_info()
            return self.send_post(key, val)


    # 获取当前处理服务器信息
    def get_now_svr_info(self):
        svr_len = len(self.svr_list)
        if svr_len <= 0:
            return None
        
        if self.now_idx >= svr_len:
            self.now_idx = 0
        return self.svr_list[self.now_idx]
    # 获取当前处理服务器信息
    def svr_now_idx_add(self):
        self.now_idx += 1
    # 删除当前服务器信息
    def remove_now_svr_info(self):
        if self.svr_list[self.now_idx]:
            del self.svr_list[self.now_idx]