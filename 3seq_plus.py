# Вариант задания с повторяющимися элементами внутри списка
numbers_list1 = input('Введите цифры первого множества через запятую: ').split(',')
numbers_list2 = input('Введите цифры второго множества через запятую: ').split(',')
for numbers in numbers_list2:
    if numbers in numbers_list1:
        numbers_list1.remove(numbers)
print('Результат: ', ', '.join(numbers_list1))