num = int(input('Digite um numero inteiro entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número' , num)
print('unidade', u)
print('dezena', d)
print('centena', c)
print('milhar', m) 