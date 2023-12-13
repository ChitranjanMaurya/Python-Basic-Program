#Import random
# from random import functionname/import random
#Choice()
from random import choice
l1 = [1,2,3,4,5,6]
print(choice(l1))
#Output: 2   

#Randint()
from random import randint
otp = randint(10000,999999)
print("Your Otp : ",otp)
#Output: Your Otp : 313163

#Shuffle()
from random import shuffle
l2 = ["Apple","Banana","Mango"]
shuffle(l2)
print(l2)
#Output: ['Banana', 'Mango', 'Apple']