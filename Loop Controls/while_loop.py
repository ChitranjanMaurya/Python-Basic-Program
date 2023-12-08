#Program using while loop
sum = 0
n = int(input("Enter a number: "))
while n>0:
  sum = sum + n
  n -= 1
  print("Sum: ", sum)
print("Bye")
#Input: Enter a number: 5
#Output: Sum:  5
#        Sum:  9
#        Sum:  12
#        Sum:  14
#        Sum:  15
#        Bye

#while loop with else part
sum=0
n=int(input("Enter a Number: "))
while n>0:
    sum=sum+n
    n-=1
    print("Sum: ",sum)
else:
    print("loop error")
print("Bye")
#Input: Enter a number: 5
#Output: Sum:  5
#        Sum:  9
#        Sum:  12
#        Sum:  14
#        Sum:  15
#        loop error
#        Bye        
