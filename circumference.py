import math

def circumference_of_circle(radius):
    return 2 * math.pi * radius


radius = float(input("Enter the radius of the circle: "))
circumference = circumference_of_circle(radius)
print(f"The circumference of the circle is: {circumference:.2f}")
