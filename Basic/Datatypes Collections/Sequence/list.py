#Creating a List
#This list Store the integer values
l1 = [1,2,3,4,5,6]
#This List Stores the String Values
l2 = ["Apple","Mango","orange"]
print("Integer List : ",l1)
print("String List : ",l2)
#Output: Integer List : [1, 2, 3, 4, 5, 6]
#Output: String List : ['Apple', 'Mango', 'orange']

#Duplicate Values in List
l1 = [1,2,3,4,5,6,1,2,3]
print("Duplicate Value :",l1)
#Output: Duplicate Value : [1, 2, 3, 4, 5, 6, 1, 2, 3]

#List Contructor
l1 = list(("Apple","Mango","Orange")) # Note there is Double Brackets
print(l1)
#Output: ['Apple', 'Mango', 'Orange']

#List Slicing
l1 = [1,2,3,4,5,6,7,8,9,10]
print("Current List : ",l1)
#Output: Current List : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Access the value of Index 1
print("Index 1 value : ",l1[1])
#Output: Index 1 value : 2
# Access the value Between index 1 to 6
print("Index Between 1 to 6 : ",l1[1:6])
#Output: Index Between 1 to 6 : [2, 3, 4, 5, 6]
# Access the value till index 6
print("Index Till 6 : ",l1[:6])
#Output: Index Till 6 : [1, 2, 3, 4, 5, 6]
# Access the last value from List
print("Last Value : ",l1[-1])
#Output: Last Value : 10

#List Item Change
x = ["Apple","Banana","Cherry","Mango","Orange","Kiwi"]
x[1:3] = ["Grapes","Watermelon"]
print("Updated List : ",x)
#Output: Updated List : ['Apple', 'Grapes', 'Watermelon', 'Mango', 'Orange','Kiwi'] 

#Insert into List
l1 = [1,2,3,4,5,6]
l1.insert(2,"Python")
print("Updated List : ",l1)
#Output: Updated List : [1, 2, 'Python', 3, 4, 5, 6]

#Extend the List
l1 = [1,2,3,4,5]
l2 = ['A','B','C','D','E']
# Extending the list of l2 into list of L1
l1.extend(l2)
print(l1)
#Output: [1, 2, 3, 4, 5, 'A', 'B', 'C', 'D', 'E']

#Remove Item from List
# remove() : This method is used to remove element from list
l1 = [1,2,3,4,5,6,7]
l1.remove(3)
print("Update List : ",l1)
#Output: Update List : [1, 2, 4, 5, 6, 7]

# pop() : This method is used to remove last value from list
l1 = [1,2,3,4,5,6,7]
l1.pop()
print("Update List : ",l1)
#Output: Update List : [1, 2, 3, 4, 5, 6]

# del() : This method is used to remove item from the index
l1 = [1,2,3,4,5,6,7]
del l1[2]
print("Update list : ",l1)
#Output: Update list : [1, 2, 4, 5, 6, 7]

# clear() : this method is used to clear the list
l1 = [1,2,3,4,5,6,7]
l1.clear()
print("Updated List : ",l1)
#Output: Updated List :  []