<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>가위바위보 게임</title>

<style>
body{
    margin:0;
    background:white;
    color:black;
    font-family:Arial, sans-serif;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

#app{
    text-align:center;
    width:100%;
}

button{
    padding:15px 30px;
    font-size:20px;
    cursor:pointer;
    margin:10px;
    border:2px solid black;
    background:white;
    border-radius:10px;
}

.choice{
    font-size:45px;
    width:90px;
    height:90px;
}

#choices{
    display:none;
}

#resultArea{
    display:none;
    margin-top:30px;
}

.emoji{
    font-size:90px;
    margin:20px;
}

#computer{
    margin-bottom:40px;
}

#player{
    margin-top:40px;
}

#result{
    font-size:40px;
    font-weight:bold;
}
</style>
</head>

<body>

<div id="app">

    <div id="startScreen">
        <button id="startBtn">시작하기</button>
    </div>

    <div id="choices">
        <button class="choice" onclick="play('가위')">✌️</button>
        <button class="choice" onclick="play('바위')">✊</button>
        <button class="choice" onclick="play('보')">✋</button>
    </div>

    <div id="resultArea">

        <div id="computer" class="emoji"></div>

        <div id="result"></div>

        <div id="player" class="emoji"></div>

        <button onclick="resetGame()">돌아가기</button>

    </div>

</div>

<script>

const emoji={
    "가위":"✌️",
    "바위":"✊",
    "보":"✋"
};

document.getElementById("startBtn").onclick=function(){
    document.getElementById("startScreen").style.display="none";
    document.getElementById("choices").style.display="block";
};

function play(player){

    const list=["가위","바위","보"];
    const computer=list[Math.floor(Math.random()*3)];

    document.getElementById("choices").style.display="none";
    document.getElementById("resultArea").style.display="block";

    document.getElementById("computer").innerHTML=emoji[computer];
    document.getElementById("player").innerHTML=emoji[player];

    let result="무승부";

    if(player==="가위"){
        if(computer==="바위"){
            result="패배";
        }else if(computer==="보"){
            result="승리";
        }
    }

    else if(player==="바위"){
        if(computer==="가위"){
            result="승리";
        }else if(computer==="보"){
            result="패배";
        }
    }

    else if(player==="보"){
        if(computer==="가위"){
            result="패배";
        }else if(computer==="바위"){
            result="승리";
        }
    }

    document.getElementById("result").innerHTML=result;
}

function resetGame(){

    document.getElementById("resultArea").style.display="none";
    document.getElementById("choices").style.display="none";
    document.getElementById("startScreen").style.display="block";

}

</script>

</body>
</html>
