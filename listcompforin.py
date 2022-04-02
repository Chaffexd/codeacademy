single_digits = range(10)
squares = []

for digits in single_digits:
  print(digits)
  squares.append(digits**2)

print(squares) 

cubes = [digits**3 for digits in single_digits]

print(cubes)

# review of list comprehension, using for and in, range