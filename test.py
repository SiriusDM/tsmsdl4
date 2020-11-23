#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="CSEDB_U201814831")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s" % data)

db.close()