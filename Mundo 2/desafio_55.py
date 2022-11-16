'''
Exercício Python 055: Faça um programa
que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
'''

menor = 0
maior = 0

for p in range (1,6):
    peso = int(input(f'Peso da {p}ª pessoa: '))
    if peso >= maior:
        maior = peso
    if p==1 or peso <= menor:
        menor = peso

print(f'O menor peso registrado foi {menor}kg')
print(f'O maior peso registrado foi {maior}kg')
    

