#Temperature converter program with conversions stored as a list of tuples 
list=[]
def CtoF():
        temp=int(input("Enter temp in C:"))
        temp1=str(temp)+" C"
        far=((temp*9/5)+32)
        far1=str(far)+" F"
        print(far,'F')
        fa=(temp1,far1)
        list.append(fa)

def FtoC():
        temp=int(input("Enter temp in F:"))
        temp1=str(temp)+" F"
        cel=(temp-32)*5/9
        cel1=str(cel)+" C"
        print(cel,'C')
        cl=(temp1,cel1)
        list.append(cl)

while True:
    ch=input("Enter your choice,c for conversion to Celsius,f for conversion to Fahrenheit,e to exit:")
    if ch=="c":
        FtoC()
    elif ch=="f":
        CtoF()
    elif ch=="e":
        print("All the conversions made",list)
        exit()
    else:
        print("Invalid")


   




