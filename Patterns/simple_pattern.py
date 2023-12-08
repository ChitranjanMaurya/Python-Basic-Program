# Patterns program using nested loops
#*
#**
#***
#****
#*****
for i in range(1,6):  #range(start point,End point,Step(Jump))
    for j in range(i):
        print("*", end="")
    print()

#reverse
#*****
#****
#***
#**
#*
for i in range(5,0,-1):
   for j in range(i):
       print("*", end="")
   print()