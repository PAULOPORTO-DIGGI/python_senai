### 7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = float(input('Digite uma nota de 0 a 10 \n'))

if (nota > 0) and (nota <=4.99):
    print('Nota Baixa')

elif (nota >= 5) and (nota <=6.99):
    print('Nota Media')

elif (nota >=7):
    print('NOta Alta')

else:
    ('Caracter inválido')
    









