class cost:

    def __init__(self, database, user_id):
        self.db = database
        self.user_id = user_id


    def add_expense(self):

        print("\n=============== ADD EXPENSE ===============")

        category = input("Enter Category: ")

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter a valid amount. ")
            return

        date = input("Enter Date (YYYY-MM-DD): ")
        description = input("Enter Description: ")

        self.db.cursor.execute("""
            insert into expenses(
            user_id, category, amount, expenses_date,
            description) values (?, ?, ?, ?, ?)
            """, (
                self.user_id,
                category,
                amount,
                date,
                description
            ))
        self.db.connection.commit()

        print("\nExpense Added Successfully. ")

    def view_expense(self):

        print("\n=============== View EXPENSES ===============")

        self.db.cursor.execute("select expenses_id, category, amount, expenses_date, description from expenses where user_id = ? order by expenses_id DESC ", (self.user_id,))

        expenses = self.db.cursor.fetchall()

        if not expenses:
            print("No expenses found. ")
            return

        for expense in expenses:
            print("----------------------------------------------")
            print("ID           :",expense[0])
            print("Category     :",expense[1])
            print("Amount       :",expense[2])
            print("Date         :",expense[3])
            print("Description  :",expense[4])


    def search_expense(self):
        print("\n========== SEARCH EXPENSE ===============")

        category = input("Enter category to search: ")

        self.db.cursor.execute("""
         select expenses_id, category, amount,
                expenses_date, description
         from expenses
         where user_id = ? AND category LIKE ?
         """, (self.user_id, "%" + category + "%"))

        expenses = self.db.cursor.fetchall()

        if not expenses:
            print("No matching expenses found.")
            return

        for expense in expenses:
            print("----------------------------------------------")
            print("ID           :",expense[0])
            print("Category     :",expense[1])
            print("Amount       :",expense[2])
            print("Date         :",expense[3])
            print("Description  :",expense[4])


    def update_expense(self):
        print("\n =============== UPDATE EXPENSE ================")
        try:
            expense_id = int(input("Enter Expense Id: "))
            amount = float(input("Enter New Amount: "))

        except ValueError:
            print("Invalid Input. ")
            return

        category = input("Enter new category: ")
        date = input("Enter new date (YYYY-MM-DD): ")
        description = input("Enter new Description: ")

        self.db.cursor.execute("""
           Update expenses 
           Set category = ?,
                amount = ?,
                expenses_date = ?,
                description = ?
           Where expenses_id = ?  And user_id = ?
           """, [
               category,
               amount,
               date,
               description,
               expense_id,
               self.user_id
           ])

        self.db.connection.commit()
        if self.db.cursor.rowcount  > 0:
            print("\nExpense updated Successfully!")
        else:
            print("\nExpense not Found. ")

    def delete_expense(self):
        print("\n================ DELETE EXPENSE ===============")
        try:
            expense_id = int(input("Enter Expense Id: "))
        except ValueError:
            print("Please enter a valid Id. ")
            return

        self.db.cursor.execute("""
          Delete from expenses
          where expenses_id = ? and user_id = ?
          """,(expense_id,self.user_id))

        self.db.connection.commit()

        if self.db.cursor.rowcount > 0:
           print("\nExpense deleted Successfully!")
        else:
            print("\nExpense Not Found.")

    
