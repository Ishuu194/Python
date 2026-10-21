# def decor(func):
#     def inner(name):
#         if name=="sunny":
#             print("Hello sunny Bad Morning.")
#         else:
#             func(name)
#     return inner

# @decor
# def wish (name):
#     print("Hello",name,"Good Morning")
# wish("Chinny")
# wish("Bunny")
# wish("sunny")
# wish("XYZ")


# task
def decorator(add):
    def main(a, b, c):

        print("Sum of two numbers =", result)

        result = result + c
        print("Sum of three numbers =", result)

    return main


@decorator
def sum(a, b):
    return a + b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum(a, b, c)