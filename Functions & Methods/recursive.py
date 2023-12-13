#Recursion Function:- The function which call itself
# Creating a function
def factorial(x):
 if x == 1:
  return 1
 else:
 # Calling recursion function
  return(x*factorial(x-1))
num = int(input("Num : "))
print("The factorial of ",num,"is : ",factorial(num))
#Input: Num : 5
#Output: The factorial of 5 is : 120