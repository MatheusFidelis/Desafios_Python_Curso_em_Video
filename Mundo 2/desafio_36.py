'''
Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte
o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. A prestação mensal
não pode exceder 30% do salário ou então o
empréstimo será negado.
'''

valor = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira o valor do salario: R$'))
anos = int(input('Em quantos anos você vai pagar: '))

vezes = anos*12
prestacao = valor/vezes
porcentagem = prestacao * 100/salario

if prestacao > salario * 0.7:
    print(f'Esse empréstimo seria com {vezes} parcelas de R${prestacao:.2f}')
    print(f'O valor da prestacao corresponde à {porcentagem:.2f}% do seu salario')
    print('Esse empréstimo não pode ser realizado')
elif prestacao <= 0:
    print('Valor incorreto. Refaça o orçamento.')
else:
    print(f'O valor da prestacao corresponde à {porcentagem:.2f}% do seu salario')
    print(f'A casa será paga em {vezes} prestações de R${prestacao:.2f}')