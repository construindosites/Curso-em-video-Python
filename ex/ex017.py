import math
cop = float(input('digite o comprimento do cateto oposto: '))
caj = float(input('digita o comprimento do cateto adjacente: '))
## hp = (cop ** 2 + caj **2) ** (1/2)
hp = math.hypot(cop, caj)
print('A hipotenusa desses valores é: ', hp)