'''
Exercício Python 071: Crie um programa
que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: considere que o caixa possui cédulas
de R$50, R$20, R$10 e R$1.

'''
print('{:^50}'.format('BEM-VINDO AO BANCO DO TETEU!'))
print('-'*50)
valor = int(input('Qual o valor a ser sacado? R$'))
n50 = n20 = n10 = n1 = 0

while True:
    
    n50 = valor // 50
    valor = valor - n50*50
    
    n20 = valor // 20
    valor = valor - n20*20
    
    n10 = valor // 10
    valor = valor - n10*10

    n1 = valor // 1
    valor = valor - n1*1
    break

print(f'Você recebeu {n50} notas de R$50')
print(f'Você recebeu {n20} notas de R$20')
print(f'Você recebeu {n10} notas de R$10')
print(f'Você recebeu {n1} notas de R$1')
print('-'*50)
print('{:^50}'.format('VOLTE SEMPRE AO BANCO DO TETEU!'))



    

    

