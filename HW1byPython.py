# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
print ('введите номер недели от 1 до 7')
number = int(input())
if number >=1 and number<=7:
    if number ==6 or number ==7:
        print('да')
    else:
        print('нет')
else:
    print('Пожалуйста, Введите число от 1 до 7')
    number2= int(input())
    if number2 ==6 or number2 ==7:
        print('да')
    else:
        print('нет')

