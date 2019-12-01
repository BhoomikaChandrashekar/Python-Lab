lst=[]
n=int(input("enter the number of elements "))
for i in range (0,n):
	ele=int(input("Enter element  "))
	lst.append(ele)
print(lst)

#Removing duplicates
def rem(lst,n):
	print("List after removing duplicates")
	newl=[]
	for i in lst:
		if i not in newl:
			newl.append(i)
	print(newl)
		
rem(lst,n)

#Reversing the list
def rev(lst,n):
	print("Reversing the list")
	newl1=[]
	for j in range(n-1,-1,-1): #j is the iterator
		newl1.append(lst[j])
	print(newl1)
rev(lst,n)

#read in alist o fnumbers
#Use one-line comprension of createa new list of even numbers
print("One line comprehension")
S=[x for x in range(10)]#reads elements in list , S is a list
M=[x for x in S if x % 2 == 0]
M.reverse()
print(M)

#Count the number of words in a given file
from collections import Counter # collections is library from which your are importing class Counter
def word(fname):
	with open(fname) as f:
		return Counter(f.read().split())
print("Number of words in the file :",word("test.txt"))

#Read a list of numbers use recursive function to find the max of n numbers 
def maximum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0],maximum(lst[1:]))

k=maximum(lst)
print("Max element is:",k)