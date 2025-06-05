rowSize = int(input('Enter the number of rows: '))
if rowSize % 2 == 0:
    HalfdiamRow = rowSize/2
else:
    HalfdiamRow = rowSize/2 + 1
space = HalfdiamRow + 1
for i in range(1, HalfdiamRow + 1):
    for j in range(1, space + 1):
        print(end='')
    space = space - 1
    num = 1
    for j in range (2*i-1):
        print(end=str(num))
        num = num + 1
    print()
space = 1
for i in range(1, HalfdiamRow):
    for j in range(space, space + 1):
        print(end=str(num))
        num = num + 1
    print()
    