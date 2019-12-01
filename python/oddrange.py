#print odd numbers in a range
def oddrange(num1,num2):
	for i in range(num1+1,num2):
		if i%2 !=0:
			print(i)
num1=input("Enter start:")
num2=input("Enter end:")
oddrange(int(num1),int(num2))
