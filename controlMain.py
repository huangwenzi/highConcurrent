



#!/usr/bin/evn python
# coding=utf-8
# 系统或三方库
from bottle import default_app, get, run, post
from bottle import static_file, request
from beaker.middleware import SessionMiddleware
import requests
import json
import sys
import os
import time
# os.chdir("..")
# print(os.getcwd())

# 自写模块
import control.dbMgr as dbMgrMd
# import dbMgr as dbMgrMd
dbMgr = dbMgrMd.dbMgr

# 电脑地址 http://127.0.0.1:10001
# 域名地址 http://thiswen.cn:10001

# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

# 加载服务器的地址
_add_svr_path = "http://127.0.0.1:11000/addSer"

# 获取值
@get('/getVal')
def getVal():
    try:
        # 短暂休眠，模拟计算消耗
        time.sleep(0.001)
        key = request.query.key
        val = dbMgr.get_val(key) or "None"
        return val
    except Exception as e:
        print('getVal, error:', e.value)
        return "-1"

# 设置值
@post('/setVal')
def setVal():
    try:
        # 短暂休眠，模拟计算消耗
        time.sleep(0.001)
        data = request.json
        key = data["key"]
        val = data["val"]
        dbMgr.set_val(key, val)
        # 不可以返回数字，会说object is not iterable
        # return 1
        return "1"
    except Exception as e:
        print('getsetValVal, error:', e.value)
        return "-1"


# 函数主入口
if __name__ == '__main__':
    argv = sys.argv
    print(argv)
    port = int(argv[1])
    app_argv = SessionMiddleware(default_app(), session_opts)
    # 通知负载均衡，服务器准备就绪
    headers = {'content-type':'application/json'}
    data = {
        'ip': "127.0.0.1",
        'port': port
    }
    response = requests.post(_add_svr_path, data=json.dumps(data),headers=headers)
    run(app=app_argv, host='0.0.0.0', port=port, debug=True, reloader=True)

