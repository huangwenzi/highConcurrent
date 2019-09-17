# 目录介绍
- control : 数据处理代码
- client : 模拟请求的客户端

# 启动文件介绍
- controlMain : 服务器启动入口
    1. 默认启动例子： python controlMain.py 10001 127.0.0.1
                    python 启动文件 服务器端口 数据库地址
    2. 如果是linux下，使用pm2管理，使用配置文件
- clientMain : 模拟客户端启动入口
    1. 默认启动例子： python clientMain.py
- lbMain : 负载均衡启动入口
    1. 默认启动例子： python controlMain.py 11000
                    python 启动文件 服务器端口 