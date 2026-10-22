from database import database
from user import user
from cost import cost
from detail import detail
from support import show_title, pause


def main():

    db = database()
    user_obj = user(db)

    show_title()

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            user_obj.register()
            pause()

        elif choice == "2":

            user_id = user_obj.login()

            if user_id:

                expense = cost(db, user_id)
                report = detail(db, user_id)

                while True:

                    print("\n========== SPENDWISE MENU ==========")
                    print("1. Add Expense")
                    print("2. View Expenses")
                    print("3. Search Expense")
                    print("4. Update Expense")
                    print("5. Delete Expense")
                    print("6. Total Expense")
                    print("7. Category-wise Expense")
                    print("8. Monthly Expense")
                    print("9. Logout")

                    option = input("Enter your choice: ")

                    if option == "1":
                        expense.add_expense()

                    elif option == "2":
                        expense.view_expense()

                    elif option == "3":
                        expense.search_expense()

                    elif option == "4":
                        expense.update_expense()

                    elif option == "5":
                        expense.delete_expense()

                    elif option == "6":
                        report.total_expense()

                    elif option == "7":
                        report.category_report()

                    elif option == "8":
                        report.monthly_report()

                    elif option == "9":
                        print("\nLogged out successfully!")
                        break

                    else:
                        print("\nInvalid choice!")

                    pause()

        elif choice == "3":

            print("\nThank you for using SpendWise!")
            db.close()
            break

        else:

            print("\nInvalid choice!")


if __name__ == "__main__":
    main()
