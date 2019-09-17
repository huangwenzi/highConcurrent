from bottle import default_app, get, run, post
from bottle import static_file, request
from beaker.middleware import SessionMiddleware
import sys
import os
# os.chdir("..")
# print(os.getcwd())

# 自写模块
import loadBalance.LBMgr as LBMgrMd
lbMger = LBMgrMd.LBMger()

# 负载均衡管理器

# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

# 添加新的服务器
@get('/addSer')
def addSer():
    try:
        data = data = request.json
        return lbMger.add_ser(data)
    except Exception as e:
        print('getVal, error:', e.value)
        return "-1"
# 获取值
@get('/getVal')
def getVal():
    try:
        key = request.query.key
        return lbMger.send_get(key)
    except Exception as e:
        print('getVal, error:', e.value)
        return "-1"
# 设置值
@post('/setVal')
def setVal():
    try:
        data = request.json
        key = data["key"]
        val = data["val"]
        return lbMger.send_post(key,val)
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