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