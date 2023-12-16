#Match Function
# Import re module first
import re
pattern = r"^abcd"
mystring = "abcdef"
x = re.match(pattern,mystring)
print(x)
#Output: <re.Match object; span=(0, 4), match='abcd'>

#Search Function
# import re module first
import re
txt = "We are learning python"
x = re.search("\s",txt) # This expression is written for searching whitespace
print("The first whitespace : ",x.start())
#Output: The first whitespace : 2
import re
txt = "The rain in Gujarat"
x = re.search("Ahmedabad",txt)
print(x)
#Output: None

#Replace Function
import re 
str1 = "@Mr_Chitranjan provide free online training."
print("Before Replace: ", str1)
result = re.sub(r"provide", "python", str1)
print("After Replace: ", result)
#Output: Before Replace:  @Mr_Chitranjan provide free online training.
#Output: After Replace:  @Mr_Chitranjan python free online training.

#Another Example of replace function
import re 
str1 = "@Mr_Chitranjan provide free online training."
print("Before Replace: ", str1)
result = re.sub(r"[a-z]", "0", str1)
print("After Replace: ", result)
#Output: Before Replace:  @Mr_Chitranjan provide free online training.
#Output: After Replace:  @M0_C000000000 0000000 0000 000000 00000000.