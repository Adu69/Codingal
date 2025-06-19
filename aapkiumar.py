try:
    age = int(input("Enter your age: "))
    print("Valid age:", age)
except ValueError:
    print("Invalid input. Age must be a whole number (integer).")
