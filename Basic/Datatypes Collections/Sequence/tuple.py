#creating a Tuple
t1 = ("Apple", "Orange", "Cherry", 1, 2, 3, 5.4)
print("Current Tuple: ", t1)
#Output: Current Tuple:  ('Apple', 'Orange', 'Cherry', 1, 2, 3, 5.4)

#Indexing/Slicing
t1 = ("Apple", "Orange", "Cherry", 1, 2, 5.4)
print("Index 1 Value: ", t1[1])
#Output: Index 1 Value:  Orange
#Accessing the value between index 1 to 5
print("Index Between 1 to 5: ", t1[1:6])
#Output: Index Between 1 to 5:  ('Orange', 'Cherry', 1, 2, 5.4)  
#Access the last value 
print("Last Value: ", t1[-1])
#Output: Last Value:  5.4
#Access the value till index 5
print("Value till: ", t1[1:6])
#Output: Value till:  ('Orange', 'Cherry', 1, 2, 5.4)

#Tuple Constructor
t3 = tuple(("apple", "mango", "cherry",)) #note the double round brackets
print(t3)
#Output: ('apple', 'mango', 'cherry')

#Convert Tuple into List
t3 = tuple(("apple", "mango", "cherry",))
x = list(t3)
print("After Convert: ", x)
print(type(x))
#Output: After Convert:  ['apple', 'mango', 'cherry'
#Output: <class 'list'>

#Add item into list
x[1] = "Kiwi"
print("Updated list: ", x)
#Output: Updated list:  ['apple', 'Kiwi', 'cherry']

#Convert list into Tuple again
y = tuple(x)
print("After Convert: ", y)
print(type(y))
#Output: After Convert:  ('apple', 'Kiwi', 'cherry')
#Output: <class 'tuple'>

#for loop with Tuple
t5 = ("Apple", "Mango", "Orange", "Kiwi")
for i in t5:
    print(i)
#Output: Apple
#        Mango
#        Orange
#        Kiwi

#while loop with Tuple
t5 = ("Apple", "Mango", "Orange", "Kiwi")
i = 0
while i < len(t5):
    print(t5[i])
    i = i +1
else:
    print("Loop Finish")
#Output: Apple
#        Mango
#        Orange
#        Kiwi
#        Loop Finish

#How to compare Tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
#check whether tuple1 is equal to tuple2
print(tuple1 == tuple2)
#Output: False

#check whether tuple1 is less than tuple2
print(tuple1 < tuple2)
#Output: True

#check whether tuple is greater than tuple2
print(tuple1 > tuple2)
#Output: False