# import test_module;
# name=input("What is your name? ");
# test_module.show(name);


# a= test_module.person1["Age"]
# print(a)

# import test_module;


#from module

# from test_module import *; #add,sub  

# a= int(input("Enter First Number:"))
# b= int(input("Enter Second Number:"))

# print("Addition=",add(a,b))
# print("Subtraction=",sub(a,b))
# print("Multipliction=",multi(a,b))


import test_module as tm;
a = int(input("Enter a:"));
b = int(input("Enter b:"));

print("Addition=",tm.additon(a,b))

