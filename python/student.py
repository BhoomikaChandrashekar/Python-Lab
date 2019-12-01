""" <q> <1> Create a python class called 'Student' having 'name','age,
as attribute along with a
    list having the marks obtained for three subjects.
    <2> create a constructor to initialize two objects of this class
    <3> create a  member function called 'display' printing the details of the
       specific object.
    <4>Ask user to enter the values for an object through an 'accept'
member functions
    <5>Display these details
"""


class Student:

    def __init__(self):
        self.lst1=[]

    def accept(self):
        self.name=input("Enter Student name :")
        self.age=input("Enter Student age :")
        #print("enter students marks")
        for i in range(0,3):
           self.lst1.append(input("enter students marks"))

    def disp(self):
        print('Name Of Student :',self.name)
        print(' Age Of Student :',self.age)
        print('Marks of the Student in three subjectis:',self.lst1)

Student1=Student()
Student2=Student()

Student1.accept()
Student2.accept()

Student1.disp()
Student2.disp()
