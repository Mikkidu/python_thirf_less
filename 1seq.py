nums=input('Введите количество цифр: ')
numbers = []
for i in int(nums):
    numbers.append(input(f'Введите {i} элемент: '))
print('Вывод: ', numbers.sort)