total = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid: "))

due = total - paid

if due > 0:
    print("Amount due:", due)
elif due == 0:
    print("No due. Bill fully paid.")
else:
    print("Overpaid by:", abs(due))
