import math
n = int(input('Введите число: '))
def sequence(n):
    number = [2]
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            number.append(num)
    return number

def get_prime(n, number):
    fact = []
    for i in number:
        while n % i == 0:
            n = n / i
            fact.append(i)
    return fact
number = sequence(n)
numbers = get_prime(n, number)
print('Простые множетели числа ',n,' равны ', numbers)



