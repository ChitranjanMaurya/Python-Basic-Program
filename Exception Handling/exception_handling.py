#Exception Create
try:
# The code which is written try block can be occur error at runtime
 a = int(input("Enter the value of A : "))
 b = int(input("Enter the value of B : "))
 c = a/b 
 print("Answer : ",c)
except Exception as e:
 # This block will run when exception occur
 print("Exception Caught : ",e)
print("Bye")
#Input: Enter the value of A : 10
#Input: Enter the value of B : 0
#Output: Exception Caught : division by zero
#Output: Bye

#Many Exception
try:
 # We have not define variable X
 print(x)
except NameError:
 print("Variable is not define")
except:
 print("Exception Caught")
#Output: Variable is not define

#How to use else with except
try:
 print(x)
except:
 print("Something went worng")
else:
 print("Nothing went worng")
#Output: Something went worng


#Finally Block
# the block which run compulsory if error occurs or not
try:
 print(x)
except:
 print("Something went worng")
finally:
 print("Finally Block")
#Output: Something went worng
#Output: Finally Block

#User Define Exception
class MyException(Exception):
 pass
c = 25
if c>5:
 raise MyException("Something went worng")
#Output: ----------------------------------------------------------------------
# -----
# MyException Traceback (most recent call 
# last)
# <ipython-input-19-a78115dfe7c2> in <module>
#  4 c = 25
#  5 if c>5:
# ----> 6 raise MyException("Something went worng")
# MyException: Something went worng