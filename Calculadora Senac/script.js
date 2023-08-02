function clearDisplay(){
    document.getElementById("display").value = "";

}
function deleteChar(){
    var displayValue = document.getElementById("display").value;
    document.getElementById("display").value = displayValue.slice(0,-1)
} 
function appendChar(char){
    document.getElementById("display").value += char;
}
function calculate(){
    var displayValue = document.getElementById("display").value;
    var result = eval(displayValue)
    document.getElementById("display").value = result
}