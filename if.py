

#if Stetments
# 1
'''a=10
if(a>0):
    print("Postive Number")

#2
a=-5
if(a<0):
    print("Negative Number")

#3
a=20
if(a%2==0):
    print("Even Number")

#4
a=13
if (a%2!=0):
    print("Odd Number")

#5
a=10
b=30
if(a<b):
    print("B is Grater Number")

#6
a=10
b=10
if(a==b):
    print("Both Numbers are equal")

#7
age=19
if(age>= 18):
    print("Your Elligble for Voting")

#8
marks=60
if(marks>=35):
    print("Your Pass")

# 9
a=25
if(a%5==0):
    print("Divisible By 5")

#10
a=5
if(a<10):
    print("Number Is Less than 10 ")


#Nested If-else
#1
a=10
if(a>0):
    print("postive Number")
    if(a%2==0):
        print("Even Number")

#2
a=9
if(a>0):
    print("Postive Number")
    if(a%2=0):
        print("Odd Number")

#3
Battery=5
if(Battery<20):
    print("Your Mobile Battery is Down")
    if(Battery<10):
        print("Please Charge Your Mobile")

#4
Bill=1500
if(Bill>1000):
    print("You Got a 50% Discount")
    if(Bill<1500):
        print("You dont got Discount")

#5
temp=35
if(temp>30):
    print("Temperture is Hot")
    if(temp>35):
        print("Temperture is very hot")'''

#type casting
 # we can change the data typein type casting
print(int(10.25))
print(int("22"))
print(int(False))






'''#nested If else
num=int(input("Enter Number"))
if(num>0):
    print("Number is Positive")
    if(num%2==0):
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Number is Negative") # 5 example'''

# lader stetment     5 example
# Find Grater Number
'''a=int(input("Enter A value"))
b=int(input("Enter B value"))
c=int(input("Enter C value"))
if(a>b and a>c):
    print("A  is a Grater Number")
elif(b>c and b>a):
    print("B is Grater Number")
else:
    print("C is Grater Number")'''

#Find Grade of Marks
marks=int(input("Enter Marks: "))
if(marks>=90):
    print("You Got A+ Grade")
elif(marks>75 and marks<90):
    print("You Got A Grade")
elif(marks>60 and marks<75):
    print("You Got B Grade")
elif(marks>35 and marks<60):
    print("You Got C Grade")
else:
    print("You are Fail")
            

# discount

amount=int(input("Enter Shooping Amount: "))
if(amount>5000):
    print("70% Discount")
elif(amount>3000 and amount<=5000):
    print("50% Discount")
elif(amount>1500 and amount<=3000):
    print("20% Discount")
else:
    print("You Dont get Discount")





