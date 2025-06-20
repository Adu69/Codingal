import random
print("There is a random number from 1 - 10 generated. You have to guess the number.")

number = random.randint(1, 10)

guess = int(input("Guess: "))
if guess == number:
    print("Correct")
elif guess < number or guess > number:
    print("Wrong")
else:
    print("Invalid input")

