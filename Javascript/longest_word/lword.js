function LongestWord(){
    str=document.getElementById("Strin").value;
    var s=str.split(' ');
    var l=0;var i;var lword;
    for (i=0;i<s.length;i++){
        if(s[i].length > l){
            l=s[i].length
            lword=s[i];
        }
    }
    document.getElementById("result").innerHTML=lword;


}