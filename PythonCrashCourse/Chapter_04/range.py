numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

#Statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehension to generate a list by using a for loop in one line
squares = [value**2 for value in range(1, 11)]

#Try it myself
for i in range(1, 21):
    print(i)

for i in range(1, 1001):
    print(i)

for i in range(1, 21, 2):
    print(i)

threes = [value * 3 for value in range(3, 31)]
print(threes)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)