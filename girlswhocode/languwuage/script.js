//insert javascript here
function toUWU() {
  var englishInput = document.getElementById('word').value;
  var uwuOUT = "";
  for (var i = 0; i < englishInput.length; i++){
    if ((englishInput.charAt(i) == 'r') || (englishInput.charAt(i) == 'l')){
      uwuOUT += "w";
    }
    else if (englishInput.charAt(i) == 'n'){
      uwuOUT += "ny";
    }
    else if (englishInput.charAt(i) == '!'){
      uwuOUT += "~ uwu";
    }
    else {
      uwuOUT += englishInput.charAt(i);
    }
  }
  document.getElementById("demo").innerHTML = uwuOUT;
  console.log(uwuOUT);
}

function hover(){
  document.getElementById("demo").style.color = "lightblue";
}

function hoveroff(){
  document.getElementById("demo").style.color = "black";
}

document.getElementById("demo").onmouseover = function(){hover()};
document.getElementById("demo").onmouseleave = function(){hoveroff()};

function enter(event) {
  if (event.keyCode == 13) {
    alert("You pressed the Enter Key");
    toUWU();
  }
}
