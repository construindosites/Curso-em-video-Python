velocidade = int(input (' Qual é  velocidade? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Você está dentro da velicidade limite')
else:
    print('Você foi multado em', multa, 'reais')
