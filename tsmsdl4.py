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
    print("|-------1.   新生入学信息增加-------------|") 
    print("|-------2.   学生信息修改    -------------|") 
    print("|-------3.   增加新课程      -------------|") 
    print("|-------4.   修改课程信息    -------------|") 
    print("|-------5.   录入学生成绩    -------------|") 
    print("|-------6.   修改学生成绩    -------------|") 
    print("|-------7.   学生成绩信息统计-------------|") 
    print("|-------8.   学生成绩排名    -------------|") 
    print("|-------9.   信息查询        -------------|") 
    print("|------10.   删除没有选课信息的课程-------|") 
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
    print("Success!")

  #  print(sql)
  #  print(Sno,Sname,Ssex,Sage,Sdept,Scholarship)
    return
def func2(cursor,db):  #修改学生信息
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
    change = input("姓名：")
    if change != '-': 
        Sname = change
        sql = """UPDATE Student SET Sname='%s' WHERE Sno='%s'"""
        cursor.execute(sql % (Sname,Sno))
        db.commit()
    change = input("性别：")
    if change != '-': 
        Ssex = change
        sql = """UPDATE Student SET Ssex='%s' WHERE Sno='%s'"""
        cursor.execute(sql % (Ssex,Sno))
        db.commit()
    change = input("年龄：")
    if change != '-': 
        Sage = int(change)
        sql = """UPDATE Student SET Sage='%d' WHERE Sno='%s'"""
        cursor.execute(sql % (Sage,Sno))
        db.commit()
    change = input("院系：")
    if change != '-': 
        Sdept = change
        sql = """UPDATE Student SET Sdept='%s' WHERE Sno='%s'"""
        cursor.execute(sql % (Sdept,Sno))
        db.commit()
    change = input("奖学金：")
    if change != '-': 
        Scholarship = change
        sql = """UPDATE Student SET Scholarship='%s' WHERE Sno='%s'"""
        cursor.execute(sql % (Scholarship,Sno))
        db.commit()
    print("Success!")
   
    return

def func3(cursor,db): #增加课程
    Cno = input("课程号：")
    Cname = input("课程名：")
    Cpno = input("先修课：")
    Ccredit = input("学分：")

    sql = """INSERT INTO Course(Cno,Cname,Cpno,Ccredit)
           VALUES('%s','%s','%s','%d') """

    cursor.execute(sql % (Cno,Cname,Cpno,int(Ccredit)))
    db.commit()
    print("Success!")
    
    return

def func4(cursor,db): #修改课程信息
    Cno = input("请输入课程号：")
    
    sql = """SELECT * FROM Course WHERE Cno = '%s'"""
    cursor.execute(sql % Cno)
    db.commit()
    results = cursor.fetchall()
    for row in results:
        Cname = row[1]
        Cpno = row[2]
        Ccredit = row[3]

    print("原课程信息:")
    print("Cno = %s,Cname = %s, Cpno = %s, Ccredit = %d" % (Cno,Cname,Cpno,Ccredit))
    print("输入您要更改的信息(不更改则输入 - )")
    change = input("课程名：")
    if change != '-': 
        Cname = change
        sql = """UPDATE Course SET Cname='%s' WHERE Cno='%s'"""
        cursor.execute(sql % (Cname,Cno))
        db.commit()
    change = input("先修课：")
    if change != '-': 
        Cpno = change
        sql = """UPDATE Course SET Cpno='%s' WHERE Cno='%s'"""
        cursor.execute(sql % (Cpno,Cno))
        db.commit()
    change = input("学分：")
    if change != '-': 
        Ccredit = int(change)
        sql = """UPDATE Course SET Ccredit='%d' WHERE Cno='%s'"""
        cursor.execute(sql % (Ccredit,Cno))
        db.commit()
    print("Success!")
    return
def func5(cursor,db): #增加学生成绩
    Sno = input("学生学号：")
    Cno = input("课程号：")
    Grade = input("成绩：")

    sql = """INSERT INTO SC(Sno,Cno,Grade)
           VALUES('%s','%s','%d') """

    cursor.execute(sql % (Sno,Cno,int(Grade)))
    db.commit()
    print("Success!")
    
    return
def func6(cursor,db): #修改学生成绩
    Sno = input("学生学号：")
    Cno = input("课程号：")
    sql = "SELECT * FROM SC WHERE Sno='%s' AND Cno = '%s'"
    cursor.execute(sql % (Sno,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results:
        Grade = row[2]

    print("原成绩:")
    print("Sno = %s,Cno = %s, Grade = %d" % (Sno,Cno,Grade))
    print("输入您要更改的信息(不更改则输入 - )")
    change = input("成绩：")
    if change != '-': 
        Grade = int(change)
        sql = "UPDATE SC SET Grade='%d' WHERE Sno='%s' AND Cno='%s'"
        cursor.execute(sql % (Grade,Sno,Cno))
        db.commit()
    print("Success!")
    return
def func7(cursor,db): #按系统计学生的平均成绩、最好成绩、最差成绩、优秀率、不及格人数
    Sdept = input("院系：")
    Cno = input("课程号：")


    #总人数
    sql = "SELECT Count(*) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno "
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results: all = row[0]

    #平均成绩
    sql = "SELECT AVG(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno"
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results: avg = row[0]

    #最好成绩
    sql = "SELECT MAX(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno"
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results: max = row[0]

    #最差成绩
    sql = "SELECT MIN(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Sno = Student.Sno"
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results: min = row[0]
    
    #优秀率
    sql = "SELECT Count(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Grade >= 90 AND Student.Sno = SC.Sno "
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results: good = row[0]

    #不及格人数
    sql = "SELECT Count(Grade) FROM SC,Student WHERE Student.Sdept='%s' AND SC.Cno='%s' AND SC.Grade < 60 AND Student.Sno = SC.Sno "
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results: soso = row[0]
    print("平均成绩：",avg)
    print("最好成绩：",max)
    print("最差成绩：",min)
    good =good/all
    print("优秀率：",good)
    print("不及格人数",soso)

    return
def func8(cursor,db): #成绩排名
    Sdept = input("院系：")
    Cno = input("课程号：")
    sql = "SELECT Student.Sno,Student.Sname,Course.Cno,Course.Cname,SC.Grade FROM Student,Course,SC WHERE Student.Sdept = '%s' AND Course.Cno = '%s' AND Course.Cno = SC.Cno AND SC.Sno=Student.Sno ORDER BY SC.Grade DESC"
    cursor.execute(sql % (Sdept,Cno))
    db.commit()
    results = cursor.fetchall()
    for row in results:
        print("学号：%s,姓名：%s,课程号：%s,课程名：%s,成绩：%s" % (row[0],row[1],row[2],row[3],row[4]))
    return
def func9(cursor,db): #学生信息查询
    Sno = input("学生学号：")
    sql = "SELECT * FROM Student WHERE Sno = '%s'"
    cursor.execute(sql % Sno)
    db.commit()
    results = cursor.fetchall()
    for row in results:
        print("学号：%s,姓名：%s,性别：%s,年龄：%s,院系：%s,奖学金：%s" % (row[0],row[1],row[2],row[3],row[4],row[5]))
    sql = "SELECT Course.* FROM SC,Course WHERE SC.Sno='%s' AND SC.Cno=Course.Cno"
    cursor.execute(sql % Sno)
    db.commit()
    results = cursor.fetchall()
    for row in results:
        print("课程号：%s,课程名：%s,先修课：%s,学分：%s" % (row[0],row[1],row[2],row[3]))
    return
def check_course(cursor,db):
    sql = """DELETE FROM Course WHERE Cno NOT IN (SELECT Cno FROM SC)"""
    cursor.execute(sql),
    db.commit()
    print("success!")
    return


def Func_select( func, cursor,db):
    if func == '1': func1(cursor,db)
    elif func == '2': func2(cursor,db)
    elif func == '3': func3(cursor,db)
    elif func == '4': func4(cursor,db)
    elif func == '5': func5(cursor,db)
    elif func == '6': func6(cursor,db)
    elif func == '7': func7(cursor,db)
    elif func == '8': func8(cursor,db)
    elif func == '9': func9(cursor,db)
    elif func == '10': check_course(cursor,db)
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