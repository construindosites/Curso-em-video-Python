from random import randint
pc = randint( 0, 5 )
n = int(input('Estou pensando em um número de 0 a 5, tente adivinhar qual é: ') )
print('Pensei no número: ', pc)
if n == pc: 
    print('Você acertou, parabéns')
else: 
    print('Você errou, pensei no {}, não em {}!'.format(  pc, n  )) 
    
