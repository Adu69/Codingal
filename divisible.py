import math
a = int(input("Enter a number: "))
if a / 20 == 0:
    print("twist")
elif a / 15 == 0:
    pass
elif a / 5 == 0:
    print("fizz")
else:
    print("The given number is not divisible by 5, 15 or 20.")
