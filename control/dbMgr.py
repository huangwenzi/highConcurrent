
# 三方库
import pymongo
import sys

# 数据库管理类
class DbMagr():
    mydb = None

    # 初始化
    def __init__(self, ip_path):
        myclient = pymongo.MongoClient("mongodb://{0}:27017/".format(ip_path))
        self.mydb = myclient["testdb"]

    # 设置值
    def set_val(self, key, val):
        # 先检查是否key值存在
        mycol = self.mydb["test"]
        old_val = mycol.find_one({"key": key})
        if old_val:
            query = { "key": key }
            newvalues = { "$set": { "val": val } }
            mycol.update_one(query, newvalues)
        else:
            mycol.insert_one({"key": key, "val": val})
        return True

    # 获取值
    def get_val(self, key):
        mycol = self.mydb["test"]
        old_val = mycol.find_one({"key": key})
        if old_val:
            return old_val["val"]
        else :
            return None

ip_path = sys.argv[2]
dbMagr = DbMagr(ip_path)