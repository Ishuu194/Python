#Exception Handling means without stoping program run code and and manage error #try #except #else #finally this are keyword in exception handling 
'''1. syntax error 2. Runtime error 
Question
1. What is Exception
2. What is the purpose of exception handling
3. what is the meaning of exception handling
try
    risky code
except
    handle the error 
else
    if does not get error then else block excuted
finally
    '''
#abnormal and gracefully execution\termination
print(10/0)


#Normal and gracefully execution\termination
#without try except
print("stmt-1")
print(10/0)
print("stmt-3")

#with try except
print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("stmt-3")



