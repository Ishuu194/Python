# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'

# a=mygen()

# print(type(a))
# print(id(a))

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num
        num=num-1
Values=countdown(5)
for x in Values:
    print(x)


'''
                      yiled and return diffrence
    ------------------------------------------------------------------------------
    |                 yiled                |        return                       |
    ------------------------------------------------------------------------------
    | 1.retrun value one by one            | 1.return a value                    |
    | 2.pause the function                 | 2. ends the function                |
    | 3.create genorators                  | 3.use in noramal function           |      real life exssmple of return is a student result you checks marks and return result
    | 4. can be continue after yiled       | 4.cannot continue after return      |       yiled     life example ticket
    | 5. use small memory                  | 5.use large memory                  |
    ------------------------------------------------------------------------------
                              print and  return
    ---------------------------------------------------------------------------------------------
    |             print()                   |              return                               |           restrorant atm return
    ---------------------------------------------------------------------------------------------         print mobile screen
    | 1.Displays output on the screen                 | 1. Sends a value back from a function   |
    | 2.Used to show information                      | 2.Used to return a result               |
    | 3.Does not store the result for further use     | 3.Result can be stored and used later   |
    | 4.Function continues after print()              | 4.Function ends after return            |
    | 5.Can be used anywhere                          | 5.Used inside a function                |
     -------------------------------------------------------------------------------------------- ''' 