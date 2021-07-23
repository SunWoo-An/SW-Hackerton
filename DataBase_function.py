from flask import Flask,render_template, redirect, request, url_for
import js2py
import sqlite3
#import json

#with open('C:\\Users\안선우\Desktop\SW 해커톤\\User.json','r',encoding='utf-8') as f:
#    json_data = json.load(f)
#print(json.dumps(json_data))

u1 = dict()

#데이터베이스를 구축하는 함수
def Data_making():
    conn = sqlite3.connect("IT.db", isolation_level = None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS User(Number INTEGER, Name text, ID text, Password text,Class TEXT,Seatnumber INTGER, Time INTEGER)")
    conn.commit()
    conn.close()
    #데이터베이스 구축 내용 1: 정수 2: 텍스
    #User(1학번, 2이름 , 2아이디, 2패스워드, 2강의실, 1자리, 1시간 )


#Data 를 데이터베이스에 넣는 함수
def Data_inserting(num, name,Id,pw,location,seat,time):
    conn = sqlite3.connect("IT.db", isolation_level = None)
    c = conn.cursor()
    c.execute("INSERT INTO User(Number,Name,ID,Password,Class,Seatnumber,Time)VALUES(?,?,?,?,?,?,?)",(num,name,Id,pw,location,seat,time))
    conn.commit()
    conn.close()

#ID 를 통해 자리 정보를 제거하는 함수
def Data_Deleting(ID_num):
    conn = sqlite3.connect("IT.db", isolation_level = None)
    c = conn.cursor()
    c.execute("DELETE FROM User WHERE ID = ?", (ID_num))
    conn.commit()
    conn.close()


#ID 를 통해 특정 정보를 가져오는 함수
def Data_Selection(text):

    conn = sqlite3.connect("IT.db",isolation_level = None)
    c = conn.cursor()
    c.execute('SELECT * FROM User WHERE ID = "%s"' % text)
    row = c.fetchone()
    u1['Number'] = row[0]
    u1['Name'] = row[1]
    u1['ID'] = row[2]
    u1['PW'] = row[3]
    u1['Class'] = row[4]
    u1['Seat'] = row[5]
    u1['Time'] = row[6]
    conn.commit()
    conn.close()

#ID 를 통해 특정 정보를 수정하는 함수
def Data_SeatChange(text):
    conn = sqlite3.connect("IT.db",isolation_level = None)
    c = conn.cursor()
    c.execute("UPDATE Seatnumber SET subject = ? Where ID = ?", text,id)
    conn.commit()
    conn.close()
