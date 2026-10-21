#                                     #String Function
# #  IMP  how reverse string without using build in function
# s='Python'
# print(s[::-1])


# # # to check given string is palliandrome or not
# a = "madam"
# print(a[::-1])

# # # Count the Number of Vowels in a gievn string
# text = input("Enter The String: ")
# num = 0
# for b in text:
#     if b in "aeiouAEIOU":
#         num = num + 1
# print("Vowels is : ",num)



# # # print the vowels in a gieven string
# text = input("Enter The String: ")
# num = 0
# for b in text:
#     if b in "aeiouAEIOU":
#         print(b)

# #print the positive index  negative index or character


# #count the frequency of the all character in string

# #count the whitespace in a given string
text = input("Enter a string: ")
count = 0
for i in text:
    if i == " ":
        count = count + 1

print("Number of whitespace:", count)

# # # using function check the  given string is palliandrome or not with user input

# #index and find   example

# #rindex and rfind examples
i = 'Rose Lilly Rose'
p = i.rfind('Rose')
print(p)

r = "mango apple mango"
m = r.rindex('apple')
print(r)


# #s=Krishna i want to convert this string into like this K|r|i|s|h|n|a
s = 'Krishna'
print('|'.join(s))

# #count()
# str = "Hello welcome"
# str2 = str.count('e')
# print(str2)


# #capitalize()
# str = 'hello'
# str1 = str.capitalize()
# print(str1)


# #lower()
# str1 = 'ISHWARI'
# str2 = str1.lower()
# print(str2)


# #upper()
# str1 = 'ishwari'
# str2 = str1.upper()
# print(str2)

# #isupper()
# str = 'Ishwari'
# str2 = str.isupper()
# print(str2)

# #islower()
# str = 'ishwari'
# str1 = str.islower()
# print(str1)

# #length()
# str='Hello'
# print(len(str))

# #replace()
# a = 'Fortune Cloud Technology' 
# b = a.replace("Fortune Cloud","Cravita")
# print(b)                                          


# #join
# str = ""
# list = ['I','s','h','w','a','r','i']
# str2 = str.join(list)
# print(str2)


# #index
# a = 'Ishwari'
# b = a.index('a')
# print(b)


# #2nd of index
# a = "Fortune cloud technology"
# b = a.index("e",1,7)
# print(b)

#deleting string
# str1 = "Ishwari"
# del str1
# print(str1)

# #Escape sequence //   Special Code
# txt = "\"string\" is the collection of character."
# print(txt)

# #partition()
# str = "Python is a Programming langauge"
# str2 = str.partition("is")
# print(str2)

# a = 'Ishwari N bonde'
# b = a.partition('N')
# print(b)

# #split()
# a = "Python is a Programming langauge"
# b = str.split()
# print(b)

#count()                              
str = "Hello welcome"
str2 = str.count('e')
print("occurences:",str2)

txt = "I love apples, apple is my favorite fruit"
x = txt.count("Are",10,24)
print(x)





# str = "Welcome to the python"
# str2 = str.index("p",14,20)
# print(str2)

