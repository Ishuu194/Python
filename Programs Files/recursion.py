# function inside the function  is called recursion it call itself and control by the condition ex folder many file inside a folder
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#local variable and global variable
virat="Cricketer"          #global variable which is accessable out side the block or fun
def sairat():
    archi="Actress"   # archi is local vairable which is accessable only inside the fun
    print(virat)
    print(archi)
sairat()


#2
flower="Rose"
def f1():
    global fruit 
    fruit="Orange"
f1()
def f2():
    print(flower)
    print(fruit)
f2()

    