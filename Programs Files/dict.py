# d={1:"Rahul",2:"abc",3:"XYZ"}
# print(d)
# print(type(d))
# print("1st Name is: "+d[1])
# print("3rd Name is: "+d[3])
# print(d.keys())
# print(d.values())


# mydict={
#     "id":101,
#     "Name":"Ishwari",
#     "Age": 22
# }
# # p=mydict.popitem()
# mydict.setdefault("City","Pune")
# print(mydict)



#Task Dictionary
students={}
for i in  range(5):
    name=input("Enter Student Name: ")
    marks=int(input("Enter Marks: "))
    students[name]=marks
print("\nStudent Data: ")
for name, marks in students.items():
    print("Name:-", name,   "Marks:-",marks)






