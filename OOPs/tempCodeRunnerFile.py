#Achieveing Encapsulation by private
# class A: # Parent Class
#  def __init__(self,a):
#   self.__a=a # the variable is a private variable
#  def show(self):
#  # Printing a private using function
#   print("Private Variable : ",self._a)
# class B(A): # Child Class
#  def __init__(self,b):
#   super().__init__(b) 
#  def showB(self):
#   print(self.__a)
# # creating an object of class B
# obj = B(20)
# obj.showB()
# #Output: it gives error because we can't access private variable in other class
