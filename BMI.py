height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg"))

BMI = weight / (height/100)**2

print("Your BMI is",BMI)

if BMI < 18.4:
    print("You are underweight")
elif BMI < 24.9:
    print("You are healthy")
elif BMI < 29.9:
    print("You are overweight")
elif BMI < 34.9:
    ("You are severely overweight")
elif BMI < 39.9:
    print("You are obese")
elif BMI < 50.00:
    print("You are severely obese")
else:
    print("GO EXERCISE YOU MORON!")
    