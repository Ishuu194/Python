# #1.Create a file named student.txt and write "Welcome to Python" into it using w mode.
# a=open("student.txt","w")
# a.write("Welcome to Python")
# a.close


#3.Open student.txt in read mode (r) and display its complete content.

# f=open("student.txt","r")
# print(f.read())
# f.close()

#4.Write a Python program to count the number of characters in student.txt
# f=open("student.txt","r")
# count=0
# for line in f:
#     count = count + len(line) 
# print("Number Of Character is=",count)
# f.close()


#5.Open student.txt in append mode (a) and add "Python File Handling" at the end of the file.

# b = open("student.txt","a")
# b.write("\nPython File Handling")
# f.close()

#6.Create a file named marks.txt and write the following:

# Python: 80
# Java: 75
# Mern Stack: 85


#7.Read marks.txt and display each line separately.
# a = open("marks.txt","r")
# print("\n",a.read())
# a.close()


#8.Create a file named message.txt using x mode and write "Hello Students" into it.
# i = open("message.txt","x")
# i.close()


#9.Open student.txt and check whether the word Python is present in the file or not.
m = open("student.txt","r")
text=0
if "Python" in text:
    print("Python word is Present in text")
else:
    print("Python word is not present in text")




#10.Create a file named numbers.txt and write numbers 1 to 10, each on a new line. Then read and display them.
# n = open("numbers.txt","r")
# print(n.read())
# n.close()

