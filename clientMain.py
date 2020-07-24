
import time

import client.clientMgr as clientMgrMd

# 模拟客户端请求
clientMgr = clientMgrMd.ClientMgr()


# 自动发请求
# num:数量
# interval:间隔时间
def auto_send(num, interval):
    now = time.time()
    idx = 0
    while idx < num:
        idx += 1
        ret = clientMgr.send_set("%d"%(idx), "%d"%(idx))
        ret = clientMgr.send_get("%d"%(idx))
        time.sleep(interval)
    end = time.time()
    print("time consume:%f"%(end - now))

while True:
    in_str = input("数量和间隔：")

    while True:
        now = time.time()
        if now < 1579081020:
            time.sleep(0.01)
        else:
            break

    str_arr = in_str.split(" ")
    num = int(str_arr[0])
    interval = float(str_arr[1])
    print("num:%d,interval:%f"%(num,interval))
    auto_send(num, interval)