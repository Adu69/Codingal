x = int(input("Enter a number"))
if (type(x) is int):
    print(x,"is an integer")
else:
    print(x,"is not an integer")

x = int(input("Enter a number"))
if(type(x)is not float):
    print("true")
else:
    print("false")


x = int(input("Enter a number"))
y = int(input("Enter a number"))
if (x is y):
    print(x,"and",y,"are same same but different")
else:
    print(x,"and",y,"are different")