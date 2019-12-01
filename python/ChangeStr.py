def ChangeStr(str1):
    #increment each alphabet by 1
   temp=""
   temp1=""
   l=len(str1)
   for i in range(0,l):
       ch=str1[i]
       if ch>="a" and ch<="z":
            if(ch=='z'):
                temp=temp+"a"
            else:
                    ch1=ord(ch)
                    ch1=ch1+1
                    temp=temp+chr(ch1)
       else:
            temp=temp+ch
   for i in range(0,l):
       ch2=temp[i]
       if (ch2=="a" or ch2=="e" or ch2=="i" or ch2=="o" or ch2=="u"):
           s=ord(ch2)
           s=s-32
           temp1=temp1+chr(s)
       else:
            temp1=temp1+ch2
   print(temp1)

ChangeStr(input("Enter the string:"))



