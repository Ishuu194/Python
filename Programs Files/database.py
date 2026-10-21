# import sqlite3 as s
# data=s.connect("mydata.db")
# m=data.cursor()
# # m.execute("create table student1(id int,name varchar(20))")
# # m.execute("insert into student1(id,name) values(?,?)",(1,'Abc'))

# l=[(2,'xyz'),(3,'opi'),(4,'uhu'),(5,'ipo')]
# m.executemany("insert into student1 values(?,?)",l)
# # dm.execute("select * from student1")
# # print(data)
# # # for row in data:
# # #     print(row[0]row[1],row[2])

# data.commit()
# data.close()



# import sqlite3 as s
# data=s.connect("mydata.db")
# m=data.cursor()
# m.execute("insert into student1(id,name) values(?,?)",(1,'Abc'))
# data.commit()
# data.close()


import sqlite3 as s
data=s.connect("mydata.db")
m=data.cursor()
l=[(2,'xyz'),(3,'opi'),(4,'uhu'),(5,'ipo')]
m.executemany("insert into student1 values(?,?)",l)
data.commit()
data.close()









