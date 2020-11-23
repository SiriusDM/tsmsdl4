#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

#Cover for User
def cover():
    print("  Welcome to Student Management System !")
    print("             Author: zhl               ")
    return
def Func_list():
    print("|-----------Function List-----------------|")
    print("|-------1.   新生入学信息增加-------------|") #insert
    print("|-------2.   学生信息修改    -------------|") #update
    print("|-------3.   增加新课程      -------------|") #insert
    print("|-------4.   修改课程信息    -------------|") #update
    print("|-------5.   录入学生成绩    -------------|") #insert
    print("|-------6.   修改学生成绩    -------------|") #update
    print("|-------7.   学生成绩信息统计-------------|") #select
    print("|-------8.   学生成绩排名    -------------|") #select
    print("|-------9.   信息查询        -------------|") #select
    print("|------10.   退出系统        -------------|") #select
    print("------------------------------------------")
    #print("Choose Function:")
    return

def func1(cursor,db):   #新生入学信息增加
    Sno = input("学生学号：")
    Sname = input("学生姓名：")
    Ssex = input("学生性别：")
    Sage = input("学生年龄：")
    Sdept = input("学生所在系：")
    Scholarship = input("是否获得奖学金：")

    sql = """INSERT INTO Student(Sno,Sname,Ssex,Sage,Sdept,Scholarship)
           VALUES('%s','%s','%s','%d','%s','%s') """

    cursor.execute(sql % (Sno,Sname,Ssex,int(Sage),Sdept,Scholarship))
    db.commit()
    print(sql)
  #  print(Sno,Sname,Ssex,Sage,Sdept,Scholarship)
    return
def func2(cursor,db):
    Sno = input("请输入学生学号：")
    
    sql = """SELECT * FROM Student WHERE Sno = '%s'"""
    cursor.execute(sql % Sno)
    db.commit()
    results = cursor.fetchall()
    for row in results:
        Sname = row[1]
        Ssex = row[2]
        Sage = row[3]
        Sdept = row[4]
        Scholarship = row[5]

    print("学生信息:")
    print("Sno = %s,Sname = %s, Ssex = %s, Sage = %d, Sdept = %s, Scholarship = %s" % (Sno,Sname,Ssex,Sage,Sdept,Scholarship))
    print("输入您要更改的信息(不更改则输入 - )")
    change = input("学号：")
    if change != 'n': Sno = change
    sql = """UPDATE Student SET Sno='%s' WHERE Sname='%s'"""
    cursor.execute(sql % (Sno,Sname))
    db.commit()
    change = input("姓名：")
    if change != 'n': Sname = change
    change = input("性别：")
    if change != 'n': Ssex = change
    change = input("年龄：")
    if change != 'n': Sage = int(change)
    change = input("院系：")
    if change != 'n': Sdept = change
    change = input("奖学金：")
    if change != 'n': Scholarship = change

   
    return

def func3(cursor):
    return
def func4(cursor):
    return
def func5(cursor):
    return
def func6(cursor):
    return
def func7(cursor):
    return
def func8(cursor):
    return
def func9(cursor):
    return

def Func_select( func, cursor,db):
    if func == '1': func1(cursor,db)
    elif func == '2': func2(cursor,db)
    elif func == '3': func3(cursor)
    elif func == '4': func4(cursor)
    elif func == '5': func5(cursor)
    elif func == '6': func6(cursor)
    elif func == '7': func7(cursor)
    elif func == '8': func8(cursor)
    elif func == '9': func9(cursor)
    else:
        return 0

def main():
    cover()
    # connect to db
    db = pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="CSEDB_U201814831")
    cursor = db.cursor()
    goon = 'n'
    while goon != 'y' :
        Func_list()
        func = input("Choose Function:")
        Func_select(func, cursor, db)
        goon = input("是否退出(y/n)：")
    db.close()
    return 
#main()

main()