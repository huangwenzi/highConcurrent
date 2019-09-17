
import time

import client.clientMgr as clientMgrMd

# 模拟客户端请求

clientMgr = clientMgrMd.ClientMgr()

clientMgr.send_post("a","b")

now = time.time()
for item in range(1000):
    clientMgr.send_get("a")
end = time.time()
print(end - now)