Amount = int(input("Enter amount for withdrawal: "))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print('100 rupee notes: ',note_1)
print('50 rupee nootes: ',note_2)
print('10 rupee notes: ',note_3)