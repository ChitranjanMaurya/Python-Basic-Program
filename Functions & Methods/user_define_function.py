#User Define Function
#Create function
def myfunction():
 print("hello")
#Calling a function
myfunction()
#Output: hello

#Function with one Arguments
# Creating a function
def myfunction(a):
 print("A : ",a)
 #Calling a Function
myfunction(10) # passing argument as a 10
#Output: A : 10

#Multiple Arguments into Function
#Creating a Function
def myfunction(a,b):
 print("A : ",a)
 print("B : ",b)
# Calling a function
myfunction(10,20) # Passing 2 arguments
#Output: A : 10
#Output: B : 20

#Keywords Arguments
# Creating a function
def myfunction(child3,child2,child1):
 print("Youngest Child is : "+child1)
# Calling a Function
myfunction(child1="Ritesh",child2="Ram",child3="Geeta")
#Output: Youngest Child is : Ritesh

#Default Parameter Value
# Creating a function
def myfunction(state="Gujarat"):
 print("I am from : "+state)
# calling a Function
myfunction("Rajasthan")
myfunction("Punjab")
myfunction("Uttar Pradesh")
myfunction()
#Output: I am from : Rajasthan
#Output: I am from : Punjab
#Output: I am from : Uttar Pradesh
#Output: I am from : Gujarat

#Passing a list into function
# Creating a function
def myfunction(fruit):
 for i in fruit:
  print(i)
f = ["Apple","Mango","Orange"]
# Calling a function
myfunction(f)
#Output: Apple
#Output: Mango
#Output: Orange

#Return Values from function
# Creating a function
def myfunction(x):
 return 5*x
# Calling a function
print(myfunction(3))
print(myfunction(4))
print(myfunction(5))
#Output: 15
#Output: 20
#Output: 25

