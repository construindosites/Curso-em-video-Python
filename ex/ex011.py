altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a lardura da parede? '))
parede = altura * largura
litro_tinta = parede / 2
print('Você precisa de {} litros para pintar essa parede'.format((litro_tinta)))
