  
from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
    return age 
      
# Driver code  
y=input("Enter th dob:")
yr=y.split("-")


print(calculateAge(date(int(yr[2]), int(yr[1]), int(yr[0]))), "years") 
