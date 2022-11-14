'''
Exercício Python 038: Escreva um programa que leia dois números
inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

if (type(n1) or type(n2)) == str:
    print('Valor inválido. Insira um número!.')

elif n1 > n2:
    print(f'{n1} é maior que {n2}')

elif n2 > n1:
    print(f'{n2} é maior que {n2}')
    
else:
    print(f'Os números são iguais')

