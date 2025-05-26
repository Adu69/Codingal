# Sasta Uber Ola
print("Choose a Vehicle")
print("1.Bike")
print("2.Car")
print("3.Metro")
choice = int(input("Enter the number of the vehicle you have chosen: "))
if choice == 1:
    print("What type of bike?")
    print("1. Motorbike (Faster but less safe)")
    print("2. Scooty (Slower but safer)")
    choice2 = int(input("Enter the number of the type of bike chosen: "))
    if choice2 == 1:
        print("You have chosen the Motorbike")
    elif choice2 == 2:
        print("You have chosen scooty")
    else:
        print("Wrong number chosen. Please choose within the given options.")
    
elif choice == 2:
    print("What type of car?")
    print("1. Maruti Suzuki Swift")
    print("2. Hyundai Creta")
    choice2 = int(input("Enter the number of the type of car chosen: "))
    if choice2 == 1:
        print("You have chosen the Suzuki Swift")
    elif choice2 == 2:
        print("You have chosen Hyundai Creta")
    else:
        print("Wrong number chosen. Please choose within the given options.")

elif choice == 3:
    print("You have choosen Metro")

else:
    print("PLEASE CHOOSE A VEHICLE FROM ONE OF THE OPTIONS GIVEN")
