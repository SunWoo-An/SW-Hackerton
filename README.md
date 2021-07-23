# SW-Hackerton
2021 KNU 컴퓨터학부 SW 해커톤


삐용삐용 팀 : 2020116575 안선우 2020114702 이예림 2020112090 이동재 2020116737 한재준


1.	주제

  COVID-19로 변화된 대학생활을 개선할 수 있는 창의적이고 혁신적인 소프트웨어
  
2.	현재 학교생활의 문제점

  시험기간 또는 자습을 위해서 빈 강의실을 사용하는 학생들이 많음.
  빈 강의실을 사용할 때 수기로 방명록을 작성해야 하는 불편함으로 방명록을 작성하지 않는 사람이 있음.
  위와 같은 사람들로 인해 이동경로를 파악하기 힘듦.
  강의실 사용시 친한 사람들끼리 같이 앉는 경우가 발생. 즉 사회적 거리두기가 잘 지켜지지 않음.
  
3.	프로그램 설명
  
  프로그램 이름 : UOEC (using program of empty class) / 실행방법 : app.py의 flask 템플릿을 이용해 서버를 연 뒤 html을 python 코드 내의 라우팅을 통해 연결하여 프로그램을 구현함.
  
  -	강의실 좌석 예약 프로그램 개발
  -	사용자가 건물 및 강의실 출입 시 앱 또는 웹 실행 -> 좌석예약 및 배정 -> 좌석이용 -> 퇴실 과정으로 이루어짐
  - 강의실 사용하기 15분 전 예약가능
  - 웹사이트 또는 앱 실행 후 로그인
  - 건물 내 사용할 수 있는 강의실에서 좌석 예약
  - 1인당 기본이용시간: 4시간 / 연장 2번 가능(한번 연장할 때마다 2시간씩 연장)
  - 이용시간이 끝나면 자동으로 퇴실처리 됨
  - 연장 / 퇴실 체크는 앱 또는 홈페이지에 따로 로그인하여 선택 가능
  - (사용자 id는 YES 통합정보시스템 아이디 및 정보 사용)
  - 건물폐쇄 시(오후 6시 이후) 좌석 전체 초기화
  - 사용자 본인의 이용기록은 본인만 따로 확인 가능
  - 모든 사용자의 이용기록은 전체 데이터베이스에 저장됨
  - 자리를 예약하지 않고 무단으로 강의실 출입할 시 제재(일정기간 동안 예약 및 사용 불가)
  
  내부 함수 및 코드 설명:
  - 파이썬 파일:

파이썬 패키지
1) Flask , render_template, url_for,redirect
2) schedule
3) sqlite3.db ( 외부프로그램 )

main 함수: 좌석 배열을 초기화 해주고 while문의 무한루프에서 예약된 스케줄을 일정시간마다 실행
exit 함수: 사용자가 퇴실을 눌렀을 때 좌석번호(Index)를 받아와서 좌석 배열을 수정함
allExit 함수: 모든 좌석을 빈자리로 만듦, 일괄 퇴실시간에 사용
reserve_f 함수: 사용자가 좌석을 예약할 경우 좌석번호를 받아와서 좌석 배열을 수정함
checktime 함수: 사용한 시간에 따라 사용시간을 2회까지 연장 하거나 퇴실시킴
  
  - Html, CSS 파일

Web 파일 구성: login.html, Register.html, home.html, class.html, uselist.html, reservation_102.html, reservation_104.html, reservation_108.html

Login.html 내부 기능: 회원가입 후 id, password를 입력하면 홈화면으로 들어가는 기능 구현
/ 미구현된 기능 : 회원가입 정보를 데이터베이스에서 불러와 기록과 일치하지 않는 아이디, 비밀번호를 치면 접속불가 기능

Register.html 내부 기능: 아이디, 비밀번호 등 정보를 모두 입력하지 않았을 때 오류팝업창 구현, 사용자 정보를 text로 입력 받고 난 후 submit버튼 누를 시 데이터베이스에 사용자정보 저장

Home.html 내부 기능: 사용자의 강의실 및 좌석 이용현황을 홈 화면에 표시, 예약 버튼을 누르면 강의실 선택화면으로 이동, 연장 및 퇴실 버튼 클릭 시 한번 더 묻는 팝업창 구현, 이용기록확인을 누를 시 사용자 개인의 좌석이용현황을 확인하는 화면으로 이동.
/ 미구현된 기능 :  데이터베이스 시간 내 연장버튼을 누를 시 이용가능시간 4시간 연장, 퇴실버튼을 누를 시 퇴실처리

Class.html 내부 기능: 각 강의실 클릭 시 강의실 좌석 배정화면으로 이동

Uselist.html 미구현된 기능 : 데이터베이스에서 사용자 개인의 좌석이용현황불러오기

Reservation_102.html, reservation_104.html, reservation_108 html 내부 기능: 각 강의실 내 사용가능한 좌석 구분하여 표시, 거리두기를 위해 사용할 수 없는 좌석은 선택불가, 뒤로가기 버튼 클릭 시 같은 건물 내의 강의실 선택화면으로 이동, 배정할 좌석 선택 시 한번 더 묻는 팝업창 구현(확인 버튼 누를 시 배정되고 home화면으로 돌아감), 마우스 커서가 올라간 부분 버튼 색깔변화 구현
/ 미구현된 기능 :  다른 사용자가 이미 예약한 좌석은 선택불가 기능
  
4.	영향 및 기대효과

  예약 없이는 강의실에 출입이 불가능하게 하여 코로나19상황에서 강의실에 출입했던 사람들의 정보 누락이 발생하지 않음.
  웹이나 앱을 통해 간편하게 강의실의 좌석을 예약, 관리를 하여 예약내역을 통해 이동경로를 파악하기 쉽게 함. (ex IT-4호관 사용시 기존의 구글폼 사용    으로 수동적인 자리배정 불편함 해소)
  예약가능 좌석을 지정하여 사회적 거리두기를 만족시키도록 함.
  
5. 개선점
  - 크누피아와 연동하여 사용자가 QR체크인을 했을때 출입한 건물의 정보를 받아 그 건물의 빈 강의실을 예약할 수 있도록 함
  - 통합정보시스템 아이디를 연동하여야 함
  - 1인당 1개의 좌석 예약하도록 조건설정 필요(+ 다른 사용자가 이미 예약한 좌석은 선택불가 기능)
  - 데이터베이스에서 사용자 개인의 좌석이용현황불러오기
  - 데이터베이스 시간 내 연장버튼을 누를 시 이용가능시간 4시간 연장, 퇴실버튼을 누를 시 퇴실처리 기능 추가
  - 회원가입 정보를 데이터베이스에서 불러와 기록과 일치하지 않는 아이디, 비밀번호를 치면 접속불가 기능추가
  - 퇴실시간(오후 6시 이후) 좌석 초기화 기능 추가
  
6. 사업화 추진 계획
  - 관리인원은 학생회측과 상의하여 매번 강의실을 관리할 수 있는 인원을 배치
  - 모바일 앱과 크누피아를 연동하여 간단하고 편리하게 예약시스템을 구축할 계획 있음
  - it 4호관에만 국한된 것이 아니라, 자습할 수 있는 공간의 자습실이라면 서비스 범위를 확장할 수 있음
  - 주요 사용 대상자는 경북대학교 학부생 및 교수, 직원들을 기준으로 함
  - 경북대학교의 트레이드에 맞게 붉은 색을 트레이드 색으로 정함
  - 퇴실 시간이 임박했을 때 카카오톡이나 다른 메신저 시스템을 통하여 알림서비스를 제공
  
  마케팅 전략:
  1. 초기 마케팅 전략
  - IT융복합관 게시판이나, 컴퓨터학부 단체 카카오톡방, 학교 커뮤니티 등을 사용하여 홍보
  - 자주 사용하는 건물을 기준으로 시범 시행
  2. 성숙단계 접근 전략
  - 수요도를 조사하여, 학교 내 서비스 가능 건물 확장
  - 도입 수요가 큰 건물을 대상으로 플랫폼을 제공
  - 학교 크누피아 앱 또는 통합정보시스템을 플랫폼과 연동 및 연계 시스템 제안
  3. 타학교 진출 전략
  - 적용 가능한 타학교를 조사하여, 이용대상자를 타학교 학부생 및 교수, 직원등으로 넓힘



유튜브 시연영상 링크: https://youtu.be/pihZFEtnEeE
