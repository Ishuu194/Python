#Function  its a block of code used to perform a perticular task and its also used for code reusebiity
#Non-Parameterize Function
# def wish():
#     print("Hello! Good Morning")
# wish()
# # print("By By")
# # wish()



# #Parameterize Function
# def add(a,b):   #a and b is Parametes
#     print("Addition of 2 Numbers",a+b)
# add(1,2)
# add(10,20)   #10 and 20 is argument
# add(100,200)
# add(1000,2000)



# #return Function
# def addition(x,y):
#     return x+y
# print(addition(20,20))


# def mult(a,b):
#     return a*b
# print(mult(2,5))


# def display(name):
#     print("My name is",name)      #required Argument
# display("Duggu")

# def hello(name,age,city):       #keyword Argument
#     print("Name:",name,"Age:",age,"City:",city)
# hello(name="Ishwari",age=22,city="Pune")


# def info(name,age,city="Pune"):    #default Argument
#     print("Name:",name,"Age:",age,"City:",city)
# info("Ishwari",22)
# info("Jagruti",25,"Mumbai")


 # 4 diffrence return and print + 1 example 
'''
    _______________________________________________________________________________________________________
    |              print	                            |            return                               |
    -------------------------------------------------------------------------------------------------------
    |   1. Print shows the answer.	                    |    1. Return gives the answer back.             |
    |   2. We use print to see the result.	            |    2. We use return to use the result again.    |
    |   3. print does not give the value back.          |    3. return gives the value back.              |
    |   4. print does not stop the function immediately.|    4. return stops the function.                |
    |______________________________________________________________________________________________________

#Example    with return keyword
def square(num):
    return num **2
print("Square is:",square(3))



#example       with print keyword
def cube(num):
    print("Cube is:",num **3)
cube(2)
'''

# #  using function check with  pallendrome or not 
# def pallindrome(num):
#     temp=num
#     rev=0

#     while num>0:
#         rem = num % 10
#         rev = rev * 10 + rem
#         num = num // 10
#     if temp == rev:
#         print("Pallindrome Number")
#     else:
#         print("Not  Pallindrome Number")

# num=int(input("Enter The Number: "))
# pallindrome(num)




# #  using function check armstrong or not
# def armstrong(num):
#     temp=num
#     sum=0

#     while num > 0:
#         rem = num % 10
#         sum = sum + rem ** 3
#         num = num // 10

#     if temp == sum:
#         print("Armstrong Number")
#     else:
#         print("Not Aramstrong Number")

# num=int(input("Enter the Number: "))
# armstrong(num) 

#Keyword variable length argument           #pass all the value in the form of dictory inside ** marks parameter
# def hello(name,**marks):            # **dictonary   ** is compalsary
#     print("Name=",name)                                
#     print("Marks=",marks)
# hello("abc",Math=70,Science=50,English=90,Marathi=80,History=60)       #alternate ("abc",50,90,80,70)


# #variable length argument      #pass al the value in the form of tuple inside * marks parameter
# def hello(name,*marks):            # * tuple
#     print("Name=",name)                                
#     print("Marks=",marks)
# hello("Abc",50,90,80,70)


# print(type(hello))



#ananymous/lambda function
#7program in lambda function
# sum=lambda x,y: x + y 
# total=sum(10,20)
# print(total)

# #1
# cube=lambda a: a**3
# total=cube(2)
# print(total)

# #2
# square=lambda b: b**2
# total=square(2)
# print(total)

#3
mode=lambda a,b: a % b
total=mode(3,9)
print(total)

#4
even=lambda x: x % 2 == 0
num=even(14)
print(num)

#5
odd=lambda y: y % 2 != 0
num=odd(77)
print(num)

#6
max=lambda i,p: i > p
num=max(11,22)
print(num)

#7
# num=int(input("Enter Number: "))
# a=lambda x: "Postive" if x > 0 else "Negative"
# print(a(num))

num=int(input("Enter Number: "))
a=lambda x: "Postive" if x > 0 else "Negative"
print(a(num))