import random
print("This is rock, paper, scissors. Paper beats rock, rock beats scissors and scissors beats paper.")
while True:
    useraction = input("Enter a choice(rock, paper, scissors): ")
    possibleaction = ['rock', 'paper', "scissors"]
    computeraction = random.choice(possibleaction)
    print(f'\n You chose {useraction} and computer chose {computeraction}.')
    if useraction == 'rock':
        if computeraction == 'paper':
            print("You lose")
        elif computeraction == "scissors":
            print("You win")
        else:
            print("Draw")
    elif useraction == 'paper':
         if computeraction == 'paper':
             print("Draw")
         elif computeraction == "scissors":
             print("You lose")
         else:
             print("You win")
    else:
        if computeraction == 'paper':
            print("You win")
        elif computeraction == "scissors":
            print("Draw")
        else:
            print("You lose")
    break