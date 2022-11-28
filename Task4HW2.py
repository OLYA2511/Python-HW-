# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
from random import Random, randint
N=int(input('Введите число N'))
List=[]
i=0
for i in range(N):
    List.append(randint(-N,N))
    i+=1
print(List)
Index1=randint(0,i-1)
Index2=randint(0,i-1)
P=List[Index1]*List[Index2]
print(List[Index1])
print(List[Index2])
print('произведение элемента номер', Index1, 'и элемента номер', Index2, 'равно', P)