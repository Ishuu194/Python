# lader stetment     5 example
# Find Greater Number
a=int(input("Enter A value: "))
b=int(input("Enter B value: "))
c=int(input("Enter C value: "))
if(a>b and a>c):
    print("A  is a Greater Number")
elif(b>c and b>a):
    print("B is Greater Number")
else:
    print("C is Greater Number")



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


#Check special symbols

ch=input("Enter Character: ")
if(ch>='0' and ch<='9'):
    print("Digit")
elif(ch>='A' and ch<='Z' or ch>='a' and ch<='z'):
    print("Character")
else:
    print("special Symbols")



#check VOwels
ch=input("Enter Vowels: ")
if(ch=='A' or ch=='a'):
    print("Character is a Vowels")
elif(ch=='E' or ch=='e'):
    print("Character is a Vowels")
elif(ch=='I' or ch=='i'):
    print("Character is a Vowels")
elif(ch=='O' or ch=='o'):
    print("Character is a Vowels")
elif(ch=='U' or ch=='u'):
    print("Character is a Vowels")
else:
    print("Character is Not a Vowels")


#Count temp
Temp=int(input("Enter Temperture: "))
if(Temp>45):
    print("Very Hot Temperture ")
elif(Temp>=40 and Temp<=30):
    print("Hot Temperture")
elif(Temp>=25 and Temp<=40):
    print("Normal Temperture")
elif(Temp>=0 and Temp<=25):
    print("Cold Temperture")
else:
    print("Wrong Temperture")




