
texto = input('Informe a sua frase:').lower().replace(' ','')

if texto == texto[::-1]:
    print('é um palindromo')
else:
    print('Não é um palíndromo')