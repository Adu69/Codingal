char = input("Enter a character: ")
print(char,"is an alphabet" if char.isalpha() and len(char) == 1 else char,"is not an alphabet")
