#  Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiusculas.
# O nome com todas as letras minusculas. 
# Quantas letras sem considerar espaços.  
# Quantas letras tem o primeiro nome.

nome = str(input('Escreva seu nome completo aqui: '))
nome_sem_espaco = nome.replace(" ", "")
print(nome.upper())
print(nome.lower())
print('Quantidade de letras do seu nome é ', len(nome_sem_espaco))
print('Quantidade de letras no seu Primeiro nome é: ' , len(nome.split()[0]))
#print(len(nome.split()[1]))
#print(len(nome.strip( " " )))
#print(len(nome))