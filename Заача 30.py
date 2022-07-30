import math
from math import pi
k = pi
print('Изначально число pi равно',pi)
k =int(input('Введите точность, с которой будет вычислено число: ')) 
number = sum(1/16 **x*(4 /(8*x  +  1) -2 /(8*x  +  4) -1 /(8 *x  +  5) -1 /(8 *x  +  6)) for x in range (k))
print(number)

