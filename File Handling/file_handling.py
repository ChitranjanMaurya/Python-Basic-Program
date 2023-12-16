#File Creating
# open("File name","Permission")
s = "This is my file handling program"
file = open("demo1.txt","w")
file.write(s)
print("File created")
file.close()
#Output: File created

#File Read
file = open("demo1.txt","r")
filecontent = file.read()
print(filecontent)
#Output: This is my file handling program

#Write a list into File
l1 = ["Python","Java","Php","Angular"]
file = open("demo2.txt","w")
file.writelines(l1)
print("File created")
file.close()
#Output: File created

#Read a list from File
file = open("demo2.txt","r")
filelist = file.readlines()
print(filelist)
#Output: ['PythonJavaPhpAngular']

#Appending the value into file
s = "Python file handling"
file = open("demo1.txt","a")
file.write(s)
print("File Updated")
file.close()
#Output: File Updated