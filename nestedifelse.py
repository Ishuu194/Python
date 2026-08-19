#NESTED IF-ELSE STETMENT
#1
'''num=int(input("Enter Any Number: "))
if(num>0):
    print("Positive Number")
    if(num%2==0):
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Negative Number")


#2
Marks=int(input("Enter Marks: "))
if(Marks>=35):
    print("Your are Pass")
    if(Marks>=75):
        print("Excellent")
    else:
        print("Good")
else:
    print("Your are Fail")


#3
Bill=int(input("Enter Bill Amount: "))
if(Bill>500):
    print("You Got Discount")
    if(Bill>1000):
        print("You Get Gift and Free Delivery")
    else:
        print("Not Get Gift")
else:
    print("You Dont Get Discount")

#4
marks = int(input("Enter Your Marks: "))
if (marks >= 60):
    print("Submit Scholarship Form")
    if (marks >= 80):
        print("Eligible for Scholarship")
    else:
        print("Passed but No Scholarship")
else:
    print("Not Eligible")


#5
Battery=int(input("Enter Mobile Battery Percentage: "))
if(Battery<=50):
    print("please Charge Your Mobile")
    if(Battery>=20):
        print("immediately Charge Your Mobile")
    else:
        print("After Some Time Your Mobile will Switch off.")
else:
    print("Dont Need to Charge Mobile")'''


#6
num=int(input("Enter Any Number"))
if(num%5==0 and num%3==0):
    print("Number is Divisible By 5 and 3")
    if(num%3==0):
        print("Number is Divisible by 3")
    else:
        print("Number is Not Divisible by 3")
else:
    print("Not Divisible by 5 and 3")