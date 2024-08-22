### 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

operacao = str(input('Escolha uma das oerações +, -, *, / \n'))

numero1 = float(input('Digite o primeiro numero'))
numero2 = float(input('Digite o segundo numero'))

if operacao == '+':
    operacao = numero1 + numero2
    print(f'Resultado da Operação {operacao}')
elif operacao == '-':
    operacao = numero1 - numero2
    print(f'Resultado da Operação {operacao}')
elif operacao == '*':
    operacao = numero1 * numero2
    print(f'Resultado da Operação {operacao}')
elif operacao == '/':
    operacao = numero1 / numero2
    print(f'Resultado da Operação {operacao}')
else:
    print('Nenhum dos valores')
    








