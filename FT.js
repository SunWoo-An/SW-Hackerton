
//클릭하였는지 안 하였는지 확인하는 함수이다. JQUERY
$(document).ready(function(){
  $(".buttons").bind("click", function(){
		alert("click " + $(this).text());
	});
  $(".buttons").bind("dblclick", function(){
		alert("double-click " + $(this).text());
  });
});

// 예약 안된 좌석을 클릭하였을 때 정보 기입란이 뜨는 함수.
function popup(){
  var url = "popup.html";
  var name = "정보 기입란";
  var option = "width = 500, height = 500, top = 100, left = 200, location = no"
  window.open(url, name, option);
}

// 색깔이 칠해져 있을 때 클릭을 못하게 하는 Function
function DontTouch(Select,num){
  var target = document.querySelector(Select);
  if(num ===  1){
    target.style.color = '#e74c3c'
    target.style.pointerEvents: none;
  }
  else{
    target.style.color = '#2ecc71';
  }
}

// 날짜 카운팅하는 함수
function Date_Counting(){
  var today = new Date(); // 현재 날짜를 가져온다
  var nowMonth = today.getMonth() +1, nowYear = today.getFullYear(), nowDay = today.getDay(), nowDate = today.getDate();
  var string = nowYear+"년"+(today.getMonth()+1)+"월 "+ nowDate + "일";
  return string;
}

// 입실 시간 카운팅하는 함수
function Time_Counting(){
  const data1 = new Date();
  return
}
