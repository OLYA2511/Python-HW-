# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
k=int(input('введите точность числа'))
number=float(input('введите десятичное число'))
for i in range(k):
    number= round(number,1)
print(number)