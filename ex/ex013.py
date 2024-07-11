salario = float(input('Digite o valor do salario atual: '))
reajuste = float(input('Digite o valor do reajuste em porcentagem: '))
reajuste_final = (reajuste / 100) * salario
salario_ajustado = salario + reajuste_final
print('O salirio atualizado é de', salario_ajustado)