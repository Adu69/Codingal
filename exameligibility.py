cond_1 = input("Do you have a medical clause? Answer Y for yes and N for no: ")
cond_2 = int(input("Enter your attendance in numerical form: "))
Y = input("Enter the same answer you entered for do you have a medical clause, but only if you said yes, if no, enter 3: ")
if cond_1 == Y:
    print("You are allowed")
elif cond_2 >= 75:
    print("You are allowed")
else:
    print("You aren't allowed")