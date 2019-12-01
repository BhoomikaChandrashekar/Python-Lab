def LetterSurround(str1):
    l=len(str1)
    flag=0
    c=str1[0]
    d=str1[l-1]
    if(c>="a" and c<="z" or(d>="a" and d<="z")):
            return False
    else:
        for i in range (0,l):
            ch=str1[i]
            if(ch>="a" and ch<="z"):
                if(str1[i-1]!="+" or str1[i+1]!="+"):
                     flag=1
                     return False
    if(flag==0):
        return True     
               
s=LetterSurround(input("Enter a string:"))
print(s)
           
        
        
     
   

     
       
           
                    
   
