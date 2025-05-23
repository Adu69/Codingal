a = int(input("Enter the speed of 1st cyclist"))
b = int(input("Enter the speed of 2nd cyclist"))
c = int(input("Enter the speed of 3rd cyclist"))

avg =( a + b + c ) / 3
print(avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than &d, &d, &d" (avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than &d, &d" (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than &d, &d" (avg, a, b, c))
elif avg > b and avg > c:
    print("%d is higher than &d, &d" (avg, c, b))
elif avg > a:
    print("%d is higher than &d" (avg, a))
elif avg > b:
        print("%d is higher than &d" (avg, b))
elif avg > c:
    print("%d is higher than &d" (avg, c))
else:
     print("Invalid input")



