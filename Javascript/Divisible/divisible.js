function Divisible(){
    n=parseInt(document.getElementById("num").value);
    if(n%3==0 && n%7==0){
        document.getElementById("result").innerHTML="Divisible by 3 and 7";
    }
    else if(n%3==0){
        document.getElementById("result").innerHTML="Divisible by 3";
    }
    else if(n%7==0){
        document.getElementById("result").innerHTML="Divisible by 7";
    }
    else{
     document.getElementById("result").innerHTML=" Not divisible by 7 or 3";

    }
   


}