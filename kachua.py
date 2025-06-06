
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
sides = 6
length = 100
angle = 360.0 / sides
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()
