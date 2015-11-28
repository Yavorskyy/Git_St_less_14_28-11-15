numbers = []
i = 2
while len(numbers) < 100:
    i += 1
    if i % 3 ==0 and i % 5 == 0:
        continue
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
        
print(numbers)
