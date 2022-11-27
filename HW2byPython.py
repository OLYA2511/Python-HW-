# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def log_no(x):
    if x==0:
        return 1;
    else:
        return 0;
x=int(input('Введите значение x(0 or 1)'))
y=int(input('Введите значение y(0 or 1)'))
z=int(input('Введите значение x(0 or 1)'))
if (x==1 or x==0) and (y==1 or y==0) and (z==1 or z==0):
    if log_no(x)*log_no(y)*log_no(z)==log_no(x)+log_no(y)+log_no(z):
        print('Истина')
    else:
        print('ложь')
else:
    print('перемнные могут принимать значение только 0 и 1')1
    