# for loop
'''#1 print 1 to 10 number
for i in range(1,11):
    print(i)



#2 print 0 to 10 number
for i in range(10,0,-1):
    print(i)'''


#3 print even number from 1 to 10
#print("Even Number")     
for i in range(1, 10):
    if i % 2 == 0:
        print(i)


#4 print odd number from 1 to 10

#print("Odd Number")      
'''for i in range(1, 10):
    if i % 2 != 0:
        print(i)


#5 even number sum in 1 to 10 
sum=0
for i in range(1,11):
    if(i%2==0):
       sum=sum+i
print("Even Number sum is:",sum)


#6 Sum of all number 1 to 10
sum=0
for i in range(1,11):
    sum= sum+i
print("Total Number sum is:",sum)


#7 odd number sum in 1 to 10 
sum=0
for i in range(1,11):
    if(i%2!=0):
       sum=sum+i
print("Odd Number sum is:",sum)


#8 Total Number of 1 to 10 Sum and then Check number is even or odd
sum=0
for i in range(1,12):
    sum=sum + i
if(sum%2==0):
    print("Sum is Even")
else:
        print("Sum is Odd")
print("Total Sum: ",sum)


#9 Find a Square of 1 to 10
square=0
for i in range(1,11):
     square = i * i
     print(i,"Square is: ",square)


#9 Find a Cube of 1 to 10
cube=0
for i in range(1,11):
     cube = i * i * i
     print(i,"cube is: ",cube)


#10 to display table of particular no
num=int(input("Enter Number: "))
for i in range(1,11):
     print(num,"*", i,"=",num*i)'''

#11 Even No square and odd number cube
for i in range(1,11):
     if i % 2 == 0:
          print(i,"Square",i**2)
     else:
          print(i,"Cube",i**3)

