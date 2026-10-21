f=open("file.txt","r")
print(f.read())
f.close()

# # # f=open("file.txt","r")
# # # print(f.readline())
# # # f.close()


# # # f=open("file.txt","r")
# # # print(f.readlines())
# # # f.close()

# # f=open("file.txt","w")
# # f.write("This is a new data\n")
# # f.write("Fortune cloud\n")
# # f.write("I want to learn Python ")
# # f.close()


# # f=open("demo.txt","x")
# # f.close()

# # #remove file with command
# # import os
# # os.remove("demo.txt")


# #check if file exists then delete it
# import os
# if os.path.exists("demofile.txt"):
#     os.remove("demo.txt")
# else:
#     print("Your File Allready exiests")


# #with statement           we dont need to close file  after using it
# with open("file.txt","r") as f:
#     content=f.read()
#     print(content)


