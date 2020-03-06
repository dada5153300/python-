
import pymysql
import time



db = pymysql.connect(host="localhost",user="root",password="123456",db="cd",port=3306,charset='utf8')

print(db)