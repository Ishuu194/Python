balance = 10000

def check_balance():
    print("Current Balance",balance)

def deposite(amount):
    global balance
    balance =  balance + amount
    print("Amount Deposite Succesfully. ")


def withdraw(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        print("Collect Your Cash. ")

    else:
        print("Insuffient Amount. ")