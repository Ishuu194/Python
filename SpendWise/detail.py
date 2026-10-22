class detail:

    def __init__(self, database, user_id):
        self.db = database
        self.user_id = user_id

    def total_expense(self):

        print("\n========== TOTAL EXPENSE ==========")

        self.db.cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        """, (self.user_id,))

        total = self.db.cursor.fetchone()[0]

        print("Total Expense: ₹", total)

    def category_report(self):

        print("\n========== CATEGORY REPORT ==========")

        self.db.cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        WHERE user_id = ?
        GROUP BY category
        """, (self.user_id,))

        data = self.db.cursor.fetchall()

        if not data:
            print("No expenses found.")
            return

        for category, amount in data:
            print(f"{category} : ₹{amount}")

    def monthly_report(self):

        print("\n========== MONTHLY REPORT ==========")

        month = input("Enter month (YYYY-MM): ")

        self.db.cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        AND expenses_date LIKE ?
        """, (self.user_id, month + "%"))

        total = self.db.cursor.fetchone()[0]

        print(f"Total expense for {month}: ₹{total}")