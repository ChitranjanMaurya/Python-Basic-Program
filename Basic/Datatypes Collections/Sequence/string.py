#Use String in Python by two way
#Single Quote in String
print('Hello World')
#Double Quote in String 
print("Hello World")
#Output: Hello World
#Output: Hello World

#Multiline String
a = """Python is booming in the Market,
Python is smart language,
Python is used in AI,Machine Learning,Data Science
"""
print(a)
#Output: Python is booming in the Market,
#Output: Python is smart language,
#Output: Python is used in AI,Machine Learning,Data Science

#Update String
a = "Hello World!"
print(a)
print("Update String : ",a[:6]+"Python")
#Output: Hello World!
#Output: Update String : Hello Python

#String Slicing
a = "Hello Python"
#Access the value of Index 1
print("Index 1 : ",a[1])
#Access the value Between index 1 to 6
print("Index between 1 to 6 : ",a[1:6])
#Access the value till index 6
print("Index till 6 : ",a[:7])
#Access the last value from String
print("Last Value : ",a[-1])
#Output: Index 1 : e
#Output: Index between 1 to 6 : ello 
#Output: Index till 6 : Hello P
#Output: Last Value : n

#String In-Built Methods
#Capitalize() : This method converts the first Character in String
a = "hello and welcome to learnvern"
x = a.capitalize()
print(x)
#Output: Hello and welcome to learnvern

#Casefold() : This method convert all Capital letter into small
a = "Hello and Welcome to Learnvern"
x = a.casefold()
print(x)
#Output: hello and welcome to learnvern

#Center() : This is use to bring your into center 
a = "Python"
print(a)
x = a.center(20)
#Update using center method
print(x)
#Output: Python
#Output:        Python 
 
#Count() : This method is used to count the repeated word in String
a = "I love Python, Python is a smart language"
x = a.count("Python")
print(x)
#Output: 2