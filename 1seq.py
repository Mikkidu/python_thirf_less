nums=input('Введите количество цифр: ')
numbers = []
for i in range(int(nums)):
    numbers.append(int(input(f'Введите {i+1}-ю цифру: ')))
numbers.sort()
print('Вывод: ', numbers)