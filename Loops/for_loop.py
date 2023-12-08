#Program using for loop
word=["Python", "Java", "React", "Nodejs"]
for i in word:
   print(i)
#Output: Python
#        Java
#        React
#        Nodejs

word=["Python", "Java", "React", "Nodejs"]
for i in word:
   print(i, '=', len(i))   #len() function is used to find the length of the string
#Output: Python = 6
#        Java = 4
#        React = 5
#        Nodejs = 6