
#non-parameterized funcction on oopas
#class
'''class student:
    def __init__(self): # init is a constrator define using init self is a variable     jevha self keyword yeto tevha to instance variable asto
        self.name="Ishwari"
        self.age=22               # this is variable intiallization
        self.marks=90

    def display(self):        # instance method accessing using self variable
        print("Name of the student is=",self.name)
        print("Age of student is=",self.age)
        print("Marks of the student is=",self.marks)

s1=student()
s1.display()'''


#parameterized constrator
# class student:
#     def __init__(self,name,age,marks): # init is a constrator define using init self is a variable     jevha self keyword yeto tevha to instance variable asto
#         self.name=name
#         self.age=age
#         self.marks=marks           #variable declaration

#     def display(self):        # instance method accessing using self variable
#         print("Name of the student is=",self.name)
#         print("Age of student is=",self.age)
#         print("Marks of the student is=",self.marks)

# s1=student()
# s1.display()
# s2=student("Abc",22,70)      #argument 
# s2.display()
'''

diff method overloading and method overwriting 5 point simple
_________________________________________________________________________________________________________________________________________
                Method Overloading	                                 |                 Method Overriding                                |
-----------------------------------------------------------------------------------------------------------------------------------------
    1]   Same method name, but different parameters.      	         |         1] Same method name and same parameters.                 |
    2]   Happens in the same class.	                                 |         2] Happens between parent and child classes.`            |
    3]   Used to perform similar tasks in different ways.	         |         3] Used to change the parent class method behavior.      |
    4]  Example: add(int a, int b) and add(int a, int b, int c)      |         4]A child class changes the parent class show() method.  |
_____________________________________________________________________|__________________________________________________________________|

'''

# compile time and run time polymorphism

#plymorphism
#method overloading

# class test:
#     def wish(self):
#         print("Hello")

#     def wish(self,a):
#         print("Hello jii")


#     def wish(self,a,b):
#         print("Hello ji kya haal chal")

# t=test()
# t.wish(1)
# t.wish(10,20)
    

# #default argument in polymorphism
# class test:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print("The sum of 3 Numbers:", a+b+c)
#         elif a!=None and b!=None:
#             print("The sum of 2 Numbers:", a+b)
#         else:
#             print("Please provide 3 or 2 Numbers")


# m=test()
# m.sum(2,3,5)

# method overriding
# class p:
#     def property(self):
#         print('Gold+Land+Cash+Power')
#     def marry(self):
#         print('APPALAMA')

# class c(p):
#     def marry(self):
#         print('Katrina Kaif')

# c=c()
# c.property()
# c.marry()



# class p:
#     def property(self):
#         print('Gold+Land+Cash+Power')
#     def marry(self):
#         print('APPALAMA')

# class c(p):
#     def marry(self):
#         super().marry()
#         print('Katrina Kaif')

# c=c()
# c.property()
# c.marry()


#constructor overriding
''' what is constructor 
why we use inheritance    we use inhertence for code reusebility
how object is created  *
what is decorated function decorator is a function which is use for function functionality
what is self variable    
'''

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Employee(person):
#     def __init__(self, name, age,eno,esal):
#         super().__init__(name, age)
#         self.eno=eno
#         self.esal=esal


#     def display(self):
#         print('Employee Name: ',self.name)
#         print('Employee Age: ',self.age)
#         print('Emplyee Number: ',self.eno)
#         print('Employee Sallaery: ',self.esal)

# e1=Employee('Chikki',22,25896,25000)
# e1.display()
# e2=Employee('Mikki',23,478515,12000)
# e2.display()


# #Abstraction                             we canit crete abstract class object if we crete it sow error  
# from abc import ABC, abstractmethod    # abc is module name and ABC is abstract base class and abstractmethof is define before set the rule
# class Car():

#     @abstractmethod                              # we can acess abstract methof using decore function @abstractmethod
#     def speed(self):
#         pass

# class BMW(Car):
#     def speed(self):
#         print("BMW Speed is 250 KM/hr")

# class Audi(Car):
#     def speed(self):
#        print("Audi speed is 200 KM/hr")

# class Thar(Car):
#     def speed(self):
#         print("Thar Speed is 150 KM/hr")

# class Creta(Car):
#     def speed(self):
#         print("Creta Speed is 100 KM/hr")

# b=BMW()
# b.speed()

# a=Audi()
# a.speed()

# t=Thar()
# t.speed()

# c=Creta()
# c.speed()



#advantages of oopes concept  
#technical example 



# #Encapsulation
# #private 
# class Fortune:
#     wifi=""
#     contact=0
#     def __init__(self):
#         self.wifi="Pagel"                      #public variable
#         self.contact=8521479630                 #public variable
#         print(self.wifi)     
#         print(self.contact)
# f=Fortune()
# print(f.wifi)
# print(f.contact)



#private access specifier
# class Fortune:
#     __wifi=""
#     contact=0
#     def __init__(self):
#         self.__wifi="Pagel"                      #public variable
#         self.contact=8521479630                 #public variable
#         print(self.__wifi)     
#         print(self.contact)
# f=Fortune()
# # print(f.__wifi)
# print(f.contact)




#proteced access specifier
class parent:
    def __init__(self):
        self._money=5000
class child(parent):
    def display(self):
        print(self.money)
c=child()
print(c._money)



# Encapsulation using private memeber
# class Rectangle:
#     __length=0              #private member
#     __breadth=0             #private member

#     def __init__(self):
#         self.__length=5
#         self.__breadth=3

#         print("Length of Rectangle is:",self.__length)
#         print("breadth of Rectangle is:",self.__breadth)

# r=Rectangle()
# # print(r.__length)
# # print(r.__breadth)




















































































































