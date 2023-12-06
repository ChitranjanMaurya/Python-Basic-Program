#1)Age>=18
#2)Weight>=50
#3)if both age and weight match with certeria then the user can donate the blood
#4)if age is less than 18 show one msg under age
#5)if weight is less than 50 show one msg under weight
#6)if age doesnot match then it should ask for weight
#Program---
age = int(input("Enter your Age : "))
if age>=18:
 weg = int(input("Enter your Weight : "))
 if weg>=50:
  print("Donate Blood")
 else:
  print("Under Weight")
else:
  print("Under Age")
#Input: Enter your Age : 19
#Input: Enter your Weight : 65
#Output: Donate Blood