a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

print(f"Initial values: a = {a}, b = {b}, c = {c}")

swap_input = input("Enter two variables to swap (e.g., a b): ").split()

if len(swap_input) == 2:
    x, y = swap_input
    if x == 'a' and y == 'b':
        a, b = b, a
    elif x == 'a' and y == 'c':
        a, c = c, a
    elif x == 'b' and y == 'c':
        b, c = c, b
    elif x == 'b' and y == 'a':
        b, a = a, b
    elif x == 'c' and y == 'a':
        c, a = a, c
    elif x == 'c' and y == 'b':
        c, b = b, c
    else:
        print("Invalid variable names.")
else:
    print("Please enter exactly two variable names to swap.")

print(f"After swap: a = {a}, b = {b}, c = {c}")
