import sqlite3
class database:
    def __init__(self):
        self.connection = sqlite3.connect("spendwise.db")
        self.cursor =  self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""Create table if not exists users(
                             user_id integer primary key AUTOINCREMENT,
                             name text not null,
                             email text unique not null,
                             password text not null)""")
        
        self.cursor.execute("""create table if not exists expenses(
                            expenses_id integer primary key autoincrement,
                            user_id int not null,
                            category text,
                            amount real not null,
                            expenses_date text not null,
                            description text ,
                            foreign key (user_id) references users(user_id))""")
        self.connection.commit()

    def close(self):
        self.connection.close()