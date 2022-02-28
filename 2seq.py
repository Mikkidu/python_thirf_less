numbers_str = input('Введите цифры списка через запятую, точку с запятой или слеш: ')
if numbers_str[1] in ',;/':
    numbers_list = numbers_str.split(numbers_str[1])
    numbers_set = set(numbers_list)
    numbers_str = ', '.join(numbers_set)
    print('Результат: ', numbers_str)
else:
    print('Ошибка. Неверно задан список.')
## Не стал все возможные ошибки учитывать.
## Программа работает корректно, если цифры вводить все через "," или все через ";" или все через "/".