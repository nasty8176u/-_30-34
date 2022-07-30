from random import randint
n=int(input('Введите размер последовательности: '))
k=int(input('Введите нижний предел последовательности: '))
l=int(input('Введите верхний предел последовательности: '))
def list1(n, k, l):
    return [randint(k, l) for i in range(n)]

def get(list):
    return [i for i in set(list)]
list2 = list1(n, k, l)
print(list2)
print(get(list2))
