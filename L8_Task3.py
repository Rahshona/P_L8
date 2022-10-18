class JustNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список(Если хотите выйти то напишите "stop"):')
        if value == 'stop':
            break
        if not value.isdigit():
            raise JustNumber(value)
        my_list.append(int(value))
    except JustNumber as ex:
        print('Вводите только числа! Это не число', ex)
print(my_list)