'''
Exercício Python 066: Crie um programa que
leia números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre
elas (desconsiderando o flag).
'''

qtd = soma = 0

while True:
    n = int(input('Insira o numero: '))
    if n == 999:
        break
    soma = soma + n
    qtd = qtd + 1

print(f'Foram inseridos {qtd} numeros e sua soma é {soma}')


    

    

