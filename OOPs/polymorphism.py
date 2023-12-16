#Method Overloading
class MO:
 def myFunction(self): # No arguments
  print("Function with no arguments")
 def myFunction(self,a): # 1 arguments
  print("Function with 1 argument")
 def myFunction(self,a,b): # 2 arguments
  print("Function with 2 arguments")
# Creating an object of Class MO
m = MO()
m.myFunction(10,20)
# Note : Method Overloading is not supported in python because python is a interperted Language
#Output: Function with 2 arguments

#Method Overriding
class MO1: # Parent Class
 def myFunction(self,a):
  print("Class MO1 function Called")
class MO2(MO1): # Child Class
 def myFunction(self,a):
  print("Class MO2 function called")
 # Super method calling the method of class MO1
  super().myFunction(10)
class MO3(MO2): # Child Class
 def myFunction(self,a):
  print("Class MO3 function called")
 # Super method calling the method of class MO2
  super().myFunction(10)
# Creating an object of class MO3
m = MO3() # Object of MO3
m.myFunction(10)
#Output: Class MO3 function called
#Output: Class MO2 function called
#Output: Class MO1 function Called