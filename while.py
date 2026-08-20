
'''# 1 print 1 to 10 Number
print("print 1 to 10 Number")
i=1
while(i<=10):
    print(i)
    i+=1

# 2 print 10 to 1 Number
print("print 10 to 1 Number")
i=10
while i>=1:
    print(i)
    i-=1


# 3 to take input from the user print reverse number
print("Revese Number")
num=int(input("Enter Number: "))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)    



#4 to take input from the user print Pallindrome Number or not
print("Pallindrome Number")
num=int(input("Enter Number: "))
rev=0
temp=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse Number is",rev)   
if(temp==rev):
    print("Given Number is Pallindrome Number")
else:
    print("Given Number is Not Pallindrome Number") 



#5 Armstrong Number
print("Armstrong Number")
num=int(input("Enter Number: "))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+rem**3  
    num=num//10
print("Sum of Number is",sum)   
if(temp==sum):
    print("Given Number is Armstrong Number")
else:
    print("Given Number is Not Armstrong Number") 


#6 Print Even Number
print("Even Number")
i=2
while(i<=10):
    print(i)
    i= i + 2



#7 Print Odd Number
print("Odd Number")
i=1
while(i<=10):
    print(i)
    i= i + 2


#8 Print Even  Number and Make there Addition
print("Even + Sum")
i=2
sum=0
while(i<=10):
    print(i)
    sum=sum+i
    i= i + 2
print("Total =",sum)


#9 Print odd  Number and Make there Addition
i=1
sum=0
while(i<=10):
    print(i)
    sum= sum+i
    i=i+2
print("Total =",sum)


#9 make there ther addition and check its even or odd
i=1
sum=0
while(i<=12):
    print(i)
    sum=sum+i
    i=i+1
print("Total =",sum)
if(sum%2==0):
    print("Even Number")
else:
    print("Odd number")


#10 find sqaure of 1 to 10
i=1
square=0
while(i<=10):
    square=i * i
    print(i,"Square is ",square)
    i=i+1  

#10 find cube of 1 to 10
i=1
cube=0
while(i<=10):
    cube=i**3
    print(i,"Cube =",cube)
    i=i+1


#11 To display table of particular number
num=int(input("Enter Any Number: "))
i=1
while(i<=10):
    print(num,"*",i,"=",num*i)
    i=i+1 '''



#12  even number square and odd number cube in 1 to 10 number
i=1
while(i<=10):
    if(i%2==0):
        print(i,"Square =",i*i)
    else:
        print(i,"Cube",i**3)
    i=i+1








