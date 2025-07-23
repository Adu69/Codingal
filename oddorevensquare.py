start = 1
end = 10
squares = [x**2 for x in range(start, end + 1)]
even_squares = [x for x in squares if x % 2 == 0]
odd_squares = [x for x in squares if x % 2 != 0]
print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
