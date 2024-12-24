try:
    numberone = int(input('Введите первое число: '))
except:
    print('Пожалуста, введите конкретное число, или цифру!')
try:
    numbertwo = int(input('Введите второе число: '))
except:
    print('Пожалуста, введите конкретное число, или цифру!')
operation=input('Введите оператор (+,-,*,/): ')
if operation == '+':
    print(numberone+numbertwo)
elif operation == '-':
    print(numberone - numbertwo)
elif operation == '*':
    print(numberone * numbertwo)
elif operation == '/':
    if numbertwo == 0:
        print('Делить на 0 нельзя! Пожалуйста, введите любое число, больше 0!')
    else:
        print(numberone / numbertwo)
else:
    print('Пожалуйста, введите один конкретный оператор из ниже указанных:')
    print('Плюс (+), минус (-), умножение (*), деление (/)')