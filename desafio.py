CONSTANTE_BONUS = 1000

nome = input('Coloque seu nome:')
salario = float(input('Coloque seu salário: '))
bonus = float(input('Coloque a porcantagem do bônus:'))

valor_bonus = (salario*bonus)+CONSTANTE_BONUS

print(f'Parábens {nome} seu bônus vai ser de {valor_bonus}')