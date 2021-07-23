from flask import Flask, render_template,redirect, request, url_for
from collections import namedtuple
import js2py
import sqlite3
import time
import schedule
import json

################################# 전체 변수 ####################################

di=0
seatCount = 100 #전체 좌석수
ary = [0] #좌석 배열, 0 : 빈자리, 1 : 사용중, 2 : 1번 연장
timeset = [0]
MyID = ""
u1 = dict()

######################### Data-Base Function 구현 ##############################

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
    
################################# WebSite 연결 #################################


app = Flask(__name__)

@app.route('/',methods = ['get','post'])
def main():
    if(request.method == 'POST'):
        #Register 정보 받아오는 코
        Name = request.form['name']
        Number = request.form['number']
        Number = int(Number)
        ID = request.form['Identity']
        PassWord = request.form['password']
        MyID = ID
        Class = ""
        Seat = 0
        Time = None
        Data_inserting(Number,Name,ID,PassWord,Class,Seat,Time)
        Data_Selection(MyID)

        #Login 과정에서 올바른 비밀번호를 쳤는지..
        
        return render_template('login.html',)
    else:
        text= ""
        return render_template('login.html')


@app.route('/register',methods=['get','post'])
def register():
    if(request.method == 'POST'):
        
        return render_template('Register.html')
    else:
        return render_template('Register.html')

@app.route('/home',methods = ['get','post'])
def home():
    if(request.method == 'POST'):
        name_input = u1.get('Name')
        time_input = u1.get('Time')
        number_input = u1.get('Number')
        return render_template('home.html',number_input = number_input,name_input = name_input , time_input = time_input)
    else:
        return render_template('home.html')

@app.route('/uselist',methods = ['get','post'])
def uselist():
    time_slip = u1.get('Time')
    return render_template('uselist.html',time_slip = time_slip)


@app.route('/class',methods = ['get','post'])
def class_all():
    if(request.method == 'POST'):
        return render_template('class.html')
    else:
        return render_template('class.html')
    
@app.route('/reserve_102',methods = ['get','post'])
def reserve_102():
    if(request.method == 'POST'):
        seatnumber = request.form['Seat']
        reserve_f(30,seatnumber)
        return render_template('reservation_102.html',ary= ary,timeset = timeset)
    else:
        return render_template('reservation_102.html')

@app.route('/reserve_104',methods = ['get','post'])
def reserve_104():
    if(request.method == 'POST'):
        seatnumber = request.form['Seat']
        reserve_f(30,seatnumber)
        return render_template('reservation_104.html',ary = ary,timeset =timeset)
    else:
        return render_template('reservation_104.html')

@app.route('/reserve_108',methods = ['get','post'])
def reserve_108():
    if(request.method == 'POST'):
        seatnumber = request.form['Seat']
        return render_template('reservation_108.html',ary = ary,timeset = timeset)
    else:
        return render_template('reservation_108.html')

if __name__ == '__main__':
    #app.debug = True
    app.run(host = "0.0.0.0",port = "8080", threaded=True)

   
########################### WebSite Function 구현 ##############################


def exit(seatNum):                      #퇴실 버튼 눌렀을때
                                        
    ary[seatNum] = 0                    #seatNum : 사용자 자리 번호
            
def allExit():                          #자리를 전부 빈자리로 만듦
    for index, value in enumerate(ary):
        if(value == 1):
            ary[index] = 0
            
def reserve_f(n,seatIndex):             #처음 예약
    if -1 < seatIndex < n:
        if ary[seatIndex] == 0:
            ary[seatIndex] = 1          #좌석 배열의 상태를 1로 만들어줌
            timeset[seatIndex] = int(time.time());
            
        else:                           #좌석이 이미 예약돼있을 경우
            1
            

    else:                               #좌석 인덱스 범위가 이상할 경우
        1
        
    return seatIndex
    
def checktime(seatIndex,state):
    global di
    timeNow = int(time.time())
    if state:                           #퇴실 안할때 
        if ary[seatIndex] == 1 or ary[seatIndex] == 2:
            timeset[seatIndex] + 7200;
        else:
            1
                                         #더이상 연장이 불가능하다.
    else:                                #퇴실할 때
        exit(seatIndex)
        timeset[seatIndex] = 0;
        
                
for i in range(0, seatCount):
    ary.append(0)
    timeset.append(0)


schedule.every().day.at("18:00").do(allExit)     #매일 18시에 allExit실행
schedule.every(10).seconds.do(checktime,seatCount)

        
seatIndex = reserve_f(seatCount,3)


while True:
    schedule.run_pending()                       #예약된 스케줄을 실행
    time.sleep(10)
    
