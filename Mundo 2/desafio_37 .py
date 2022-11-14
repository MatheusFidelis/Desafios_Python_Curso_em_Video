'''
Exercício Python 037: Escreva um programa em Python
que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário,
2 para octal e 3 para hexadecimal.
'''

num = int(input('Insira o número para ser convertido: '))

print('\nESCOLHA A BASE DE CONVERSÃO:')
print('(1) Binário')
print('(2) Octal')
print('(3) Hexadecimal')
escolha = int(input('Resposta: '))

if escolha == 1:
    num_binario = str(bin(num)).upper()[2:]
    print(f'Seu número em binário é {num_binario}')
elif escolha == 2:
    num_binario = str(octal(num)).upper()[2:]
    print(f'Seu número em octal é {num_octal}')
else:
    num_hex = hex(num).upper()[2:]
    print(f'Seu número em hexadecimal é {num_hex}')
   