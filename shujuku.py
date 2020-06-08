#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","123456","tetris" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# SQL 查询语句
sql = "SELECT * FROM highscorelist"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[1]
      score = row[2]
       # 打印结果
      print ("id=%s,name=%s,score=%s" % (id, name, score))
except:
   print ("Error: unable to fetch data")
 
# 关闭数据库连接
db.close()