class user:
    def __init__(self,database):
        self.db = database

    def register(self):
        print("\n=============== REGISTER ===============")

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

         

        try:

            self.db.cursor.execute("""
                insert into users (name, email, password)
                values(?, ?, ?)
                """,(name, email, password))

            self.db.connection.commit()

            print("\n Registration successfull !")

        except Exception as e:
            print("\n Registration failed. ")
            print("Error:",e)


    def login(self):
        print("\n=============== LOGIN ===============")

        email = input("Enter email: ")
        password = input("Enter password: ")

        self.db.cursor.execute("""
         select user_id, name
         from users
         where email = ? and password = ?
         """, (email, password))

        user = self.db.cursor.fetchone()

        if user:
            print(f"\n WELCOME , {user[1]}!")
            return user[0]

        print("\n Invalid email or password.")
        return None
            