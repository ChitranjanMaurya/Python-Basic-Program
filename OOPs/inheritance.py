#Single Inheritance
class ParentClass: # Parent Class
 def myfunction1(self): # Parent Class Property
  print("Parent Class Function Called")
class ChildClass(ParentClass): # Child Class which inhrit Parent Class
 def myfunction2(self): # Child Class Property
  print("Child Class Function Called")
# Creating an object of ChildClass
c1 = ChildClass()
c1.myfunction1()
c1.myfunction2()
#Output: Parent Class Function Called
#Output: Child Class Function Called

#Multilevel Inheritance
class A: # Parent Class
 def myFunct(self):
  print("Class A function called")
class B(A): # Sub-Parent Class
  def myfunction2(self):
   print("Class B function called")
class C(B): # Child Class
 def myfunction3(self):
  print("Class C function called")
# Creating an object of Class C
c1 = C()
c1.myFunct()
c1.myfunction2()
c1.myfunction3()
#Output: Class A function called
#Output: Class B function called
#Output: Class C function called

#Multiple Inheritance
class A1:# 1st Parent Class
 def myfunction1(self):
  print("Class A1 function called")
class B1: #2nd Parent Class
 def myfunction2(self):
  print("Class B1 function called")
class C1(A1,B1): # Child Class
 def myfunction3(self):
  print("Class C1 function called")
# Creating an object of Class c1
c1 = C1()
c1.myfunction1()
c1.myfunction2()
c1.myfunction3()
#Output: Class A1 function called
#Output: Class B1 function called
#Output: Class C1 function called

#Hierarchical Inheritance
class A1: # Parent Class
 def myFunction1(self):
  print("Class A1 Function Called")
class A2(A1): # Child Class
 def myFunction2(self):
  print("Class A2 Function Called")
class A3(A1): # Child Class
 def myFunction3(self):
  print("Class A3 Function called")
# Creating 2 objects 1 for class A2 and 1 for class A3
a2 = A2()
a3 = A3()
a2.myFunction1() # Function of Class A1
a2.myFunction2() # Function of Class A2
a3.myFunction1() # Function of Class A1
a3.myFunction3() # Function of Class A3
#Output: Class A1 Function Called
#Output: Class A2 Function Called
#Output: Class A1 Function Called
#Output: Class A3 Function called

#Hybrid Inheritance
class B1: # Parent Class
 def myFunction1(self):
  print("Function of class B1")
class B2(B1): # Child Class
 def myFunction2(self):
  print("Function of class B2")
class B3(B1): # Child Class
 def myFunction3(self):
  print("Function of class B3")
class B4(B2,B3): # Child Class
 def myFunction4(self):
  print("Function of class B4")
# Creating an object of class B4
b = B4() # Object of B4 class
b.myFunction1()
b.myFunction2()
b.myFunction3()
b.myFunction4()
#Output: Function of class B1
#Output: Function of class B2
#Output: Function of class B3
#Output: Function of class B4