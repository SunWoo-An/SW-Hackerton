from flask import Flask, render_template
import schedule
import time


di=0
seatCount = 100 #전체 좌석수
ary = [0] #좌석 배열, 0 : 빈자리, 1 : 사용중, 2 : 1번 연장
timeset = [0]
    
def exit_f(seatNum): #퇴실 버튼 눌렀을때 #seatNum : 사용자 자리 번호
    ary[seatNum] = 0
            
def allExit_f(): #자리를 전부 빈자리로 만듦
    for index, value in enumerate(ary):
        if(value == 1):
            ary[index] = 0
            
def reserve_f(n,seatIndex): #처음 예약
    if -1 < seatIndex < n:
        if ary[seatIndex] == 0:
            ary[seatIndex] = 1#좌석 배열의 상태를 1로 만들어줌
            timeset[seatIndex] = int(time.time());
        elif ary[seatIndex] == 5:#코로나 좌석을 5로 표현했기 때문
            1
        else:#좌석이 이미 예약돼있을 경우
            1
            

    else:#좌석 인덱스 범위가 이상할 경우
        1
    return seatIndex
    
def checktime_f(seatCount,state):
    global di
    timeNow = int(time.time())


    for i in range(0, seatCount):
        if ary[i] == 1 or ary[i] == 2 :#연장을 두번 이하로 했다면
            di = timeNow - timeset[i]#현재 시간과 예약 시간의 차
            if 14100< di <= 14400:

                if state == 'y':
                    timeset[i] = timeset[i] + 7200#2시간 연장
                    ary[i] = ary[i] + 1
                elif state == 'n':
                    ary[i] = 3
        else:#연장을 이미 두번 했다면, 혹은 연장할거냐는 질문에 n으로 대답했다면 (ary[i] = 3)
            if di > 14400:
                ary[i] = 0
                timeset[i] = 0
                1#퇴실시켜야함


for i in range(0, seatCount):
    ary.append(0)
    timeset.append(0)

schedule.every().day.at("18:00").do(allExit) #매일 18시에 allExit실행
schedule.every(10).seconds.do(checktime,seatCount)

        
seatIndex = reserve(seatCount,num)


while True:
    schedule.run_pending() #예약된 스케줄을 실행
    time.sleep(10)



