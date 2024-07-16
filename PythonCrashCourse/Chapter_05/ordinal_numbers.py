numbers = []
for i in range(1,10):
    numbers.append(i)
print(numbers)

for value in range(0, 9):
    if numbers[value] == 1:
        numbers[value] = f'{numbers[value]}st'
    elif numbers[value] == 2:
        numbers[value] = f'{numbers[value]}nd'
    elif numbers[value] == 3:
        numbers[value] = f'{numbers[value]}rd'
    else:
        numbers[value] = f'{numbers[value]}th'
        
print(numbers)