i = int(input("Enter a number: "))
sum = 0

a = i
while 0 < a:
    digit = a % 10
    sum += digit ** 3
    a //= 10

if i == sum:
    print(i,"is an armstrong numero")
else:
    print(i,"is not an armstrong number")

