try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma: "))
    if num1 > num2:
        result = num1 / num2
        print(result)
    else:
        result = num2 / num1
        print(result)
except ValueError:
    print("ENTER NUMBERS YOU TWAT YOU AREN'T FUNNY")
except ZeroDivisionError:
    print("At least this is an honest mistake.. Enter a non-zero number please")
except SyntaxError:
    print("Enter commas like this:1, 2")
else:
    print("No Exceptions. Proud of you :)")
finally:
    print("This will execute no matter what")

