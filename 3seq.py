#Вариант задания с неповторяющимися элементами внутри списка
numbers_str1 = input('Введите цифры первого множества через запятую: ')
numbers_set1 = set(numbers_str1.split(','))
numbers_str2 = input('Введите цифры второго множества через запятую: ')
numbers_set2 = set(numbers_str2.split(','))
print('Результат: ', ', '.join(numbers_set1-numbers_set2))