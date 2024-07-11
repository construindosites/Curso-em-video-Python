valor_produto = float(input('Valor do produto? '))
desconto = float(input('valor do desconto em porcentagem? '))
desconto_final = (desconto / 100) * valor_produto
produto_desconto = valor_produto - desconto_final
print('Com desconto o produto fica por', produto_desconto)