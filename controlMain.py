



#!/usr/bin/evn python
# coding=utf-8
# 系统或三方库
from bottle import default_app, get, run, post
from bottle import static_file, request
from beaker.middleware import SessionMiddleware
import sys
import os
# os.chdir("..")
# print(os.getcwd())

# 自写模块
import control.dbMgr as dbMgrMd
# import dbMgr as dbMgrMd
dbMagr = dbMgrMd.dbMagr

# 电脑地址 http://127.0.0.1:10001
# 域名地址 http://thiswen.cn:10001

# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

# 获取值
@get('/getVal')
def getVal():
    try:
        key = request.query.key
        print(key)
        val = dbMagr.get_val(key)
        return val
    except Exception as e:
        print('getVal, error:', e.value)
        return "-1"

# 设置值
@post('/setVal')
def setVal():
    try:
        data = request.json
        print(data)
        key = data["key"]
        val = data["val"]
        dbMagr.set_val(key, val)
        print(10)
        # 不可以返回数字，会说object is not iterable
        # return 1
        return "1"
    except Exception as e:
        print('getsetValVal, error:', e.value)
        return "-1"


# 函数主入口
if __name__ == '__main__':
    # argv = sys.argv
    # print(argv)

    prot = int(sys.argv[1])
    app_argv = SessionMiddleware(default_app(), session_opts)
    run(app=app_argv, host='0.0.0.0', port=prot, debug=True, reloader=True)
