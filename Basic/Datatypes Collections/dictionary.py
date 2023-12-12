#Creating a Dictionary
d1 = {1:"Apple",2:"Mango",3:"Orange",4:"Apple",'A':'B'}
print(d1)
# Datatype of Dictionary
print(type(d1))
#Output: {1: 'Apple', 2: 'Mango', 3: 'Orange', 4: 'Apple', 'A': 'B'}
#Output: <class 'dict'>

#List into Dictionary Store
# Storing a list into Dictionary on a single key
d2 = {1:"Python",2:"Java","fruit":["Apple","Orange","Mango"]}
print(d2)
#Output: {1: 'Python', 2: 'Java', 'fruit': ['Apple', 'Orange', 'Mango']}

#Tuple into Dictionary Store
# Storing a tuple into Dictionary on a single key
d3 = {1:"Python",2:"Java","Language":("Java","Python","Php")}
print(d3)
#Output: {1: 'Python', 2: 'Java', 'Language': ('Java', 'Python', 'Php')}

#Access the value of Dictionary
d1 = {1:"Apple",2:"Mango",3:"Orange",4:"Apple",'A':'B'}
# Access the value using Key
x = d1[3]
print(x)  #Output: Orange
# Access the value using get()
y = d1.get(1)
print(y)  #Output: Apple
# Access the value using item()
z = d1.items()
print(z)
#Output: dict_items([(1, 'Apple'), (2, 'Mango'), (3, 'Orange'), (4, 'Apple'), ('A', 'B')])
# Access the only keys from Dictionary
k = d1.keys()
print("Keys : ",k)
#Output: Keys : dict_keys([1, 2, 3, 4, 'A'])

#Change the value
d1 = {1:"Apple",2:"Mango",3:"Orange",4:"Apple",'A':'B'}
d1[3] = "kiwi"
print("Update Dict : ",d1)
#Output: Update Dict : {1: 'Apple', 2: 'Mango', 3: 'kiwi', 4: 'Apple', 'A': 'B'}
# Update dictionary by using update method
d1.update({2:"Banana"})
print("Update Dict : ",d1) 
#Output: Update Dict : {1: 'Apple', 2: 'Banana', 3: 'kiwi', 4: 'Apple', 'A': 'B'}

#Remove values from Dictionary
# Using pop()
d1 = {1:"Apple",2:"Mango",3:"Orange",4:"Apple",'A':'B'}
d1.pop(2)
print("Update Dict : ",d1)
#Output: 
# Using popitem()
d1.popitem()
print("Update Dict : ",d1)
#Output: 
#Using del()
del d1[1]
print("Update Dict : ",d1)
#Output: Update Dict :  {3: 'Orange', 4: 'Apple'}
#Using Clear()
d1.clear()
print("Update Dict : ",d1)
#Output: Update Dict :  {}
