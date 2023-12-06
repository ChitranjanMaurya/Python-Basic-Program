#1)Percentange greater than 70 == Dist
#2)Percentage greater or equalto 65 and Less than 70 == 1st Class
#3)Percentage greater or equalto 60 and Less than 65 == 2st Class
#4)Percentage greater or equalto 55 and Less than 60 == 3st Class
#5)Percentange less than 55 == Fail
p = int(input("Enter your percentange : "))
if p>=70:
 print("Dist")
elif p>=65 and p<70:
 print("1st Class")
elif p>=60 and p<65:
 print("2nd Class")
elif p>=55 and p<60:
 print("3rd class")
else:
 print("Fail")
#Input: Enter your percentange : 45
#Output: Fail