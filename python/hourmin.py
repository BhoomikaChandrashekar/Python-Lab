#Print the time entered in mins in 'hours:mins'
def HourMinute(num):
	if(int(num) <60):
		print("0:",num)
	else:
		hours=int(num)/60
		mins=int(num)%60
		print(int(hours),":",mins)

HourMinute(input("enter mins:"))
		
