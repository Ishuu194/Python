import atm

while True:
    print("--------------ATM Menu--------------")
    print("1. Check Balance")
    print("2. Deposite Amount")
    print("3. Withdraw Money")
    print("0. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = int(input("Enter deposite amount: "))
        atm.deposite(amount)

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        atm.withdraw(amount)

    elif choice == 0:
        print("Thank for using ATM.")

    else:
        print("Invalid Choice")

