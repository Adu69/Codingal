# Electricity Bill
units = int(input("Enter the number of units used in numerical form: "))
if units <= 50:
    costperunit = 2.60
    Tax = 25
    print("Your cost per unit is",costperunit)
    print("Tax charged is",Tax)
    print("Your final bill is",(units * costperunit) + Tax )

elif units <= 100 and units > 50:
    costperunit = 3.25
    Tax = 35
    print("Your cost per unit is",costperunit)
    print("Tax charged is",Tax)
    print("Your final bill is",(units * costperunit) + Tax )

elif units > 100 and units <= 200:
    costperunit = 5.26
    Tax = 45
    print("Your cost per unit is",costperunit)
    print("Tax charged is",Tax)
    print("Your final bill is",(units * costperunit) + Tax )
else:
    costperunit = 8.45
    Tax = 75
    print("Your cost per unit is",costperunit)
    print("Tax charged is",Tax)
    print("Your final bill is",(units * costperunit) + Tax )