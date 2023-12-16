#Create a Class
class myclass:
 x = 5 # Property of class
print(myclass)
#Output: <class '__main__.myclass'>

#Create object
class myclass:
 x = 5 # Property of class
# creating object of myclass
m1 = myclass() # m1 is an object of class myclass
print(m1.x)
#Output: 5

#Calling a function by object
class myclass:
 def myfunction(self): # Property of myclass
  print("Hello myFunction")
# Creating an object
m1 = myclass()
m1.myfunction()
#Output: Hello myFunction

#Create constructor
class myclass:
 # Creating a constructor
 def __init__(self):
  print("This is my constructor")
# creating an object
m1 = myclass()
#Output: This is my constructor

#Change the value by object
class myclass:
 def __init__(self,name,age):
  self.name = name
  self.age = age

 def myfunction(self):
  print("My Name is : "+self.name)
# creating an object
m1 = myclass("Sumit",25)
m1.age
m1.name

# Changing the age using object
m1.age = 26
print("Age : ",m1.age)
# Delete the object
del m1.age
print("Age : ",m1.age)
#Output: Age : 26
#Output: ----------------------------------------------------------------------
# -----
# AttributeError Traceback (most recent call 
# last)
# <ipython-input-18-75f7baa75976> in <module>
#  19 # Delete the object
#  20 del m1.age
# ---> 21 print("Age : ",m1.age)
# AttributeError: 'myclass' object has no attribute 'age'