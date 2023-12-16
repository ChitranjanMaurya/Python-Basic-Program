class RBI: # Abtract Class
 def Interest(self): # Abstract Method
  pass
class SBI(RBI): # Child Class
 def Interest(self): # RBI Interest Implements here
  print("SBI Interest is 5%")
class HDFC(RBI): # Child Class
 def Interest(self): # RBI Interest Implements here
  print("HDFC Interest is 2%")
# Creating an object of CLass SBI
s = SBI()
# Creating an object of Class HDFC
h = HDFC()
s.Interest() # SBI Interest Method Called
h.Interest() # HDFC Interest Method Called
#Output: SBI Interest is 5%
#Output: HDFC Interest is 2%


class Animal: # Abstract Class/Parent Class
 def move(self): # Abstract Method
  pass
class Dog(Animal): # Child Class
 def move(self): # Class Animal Implements method here
  print("I can bark")
class Snake(Animal): # Child Class
 def move(self):
  print("I can hisss")
# Creating an object of Class Dog
d = Dog()
# Creating an object of class Snake
s = Snake()
d.move() 
s.move() 
#Output: I can bark
#Output: I can hisss