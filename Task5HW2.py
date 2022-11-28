# Реализуйте алгоритм перемешивания списка.
import random

list = [random.randint(0,10) for i in range(random.randint(5,10))]
print(f"исходный список: {list}")
random.shuffle(list)
print(f"список после перемешивания:{list}")