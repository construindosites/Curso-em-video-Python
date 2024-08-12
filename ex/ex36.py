valorCasa = int(input('Qual o valor da casa? '))
salario = float(input('Quanto você ganha por mês? '))
tempo = int(input('Em quanto anos deseja quitar o emprestimo? '))
valorEmprestimoMes = valorCasa / (tempo * 12)
percentual_salario = salario * 0.3
if valorEmprestimoMes > percentual_salario:
    print ('você não pode pegar um emprestimo')
else:
    print ('você pode pegar um emprestimo, entre em contato com nosso banco.')
# Calculando 30% do salário
#print('Valor da prestação mensal: {:.2f}'.format(valorEmprestimoMes))
#print('30% do seu salário: {:.2f}'.format(percentual_salario))