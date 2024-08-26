# METODO - capitalize - Deixa a primeira letra maiúscula transforma toda string em minúsculo.


# texto = 'Paulo Ivo Porto    '

# texto.capitalize()

# texto2 = texto.capitalize()

# print(texto.capitalize())
# print(texto2)

### lower padroniza a string em minuscúlo

# nome = 'Paulo Ivo Porto'
# nome2 = 'PaUlo IVO porto'


# if nome.lower() == nome2.lower():
#     print('são iguais')
# else:
#     print('Não são iguais')


######## UPPER padronixa uma string em maiúscula

# print(nome.upper())

#### replace muda um padrão de caracteres de uma string

# silvano_sales = 'coração canção função'

# silvano_sales2 = silvano_sales.replace('ç', 'c')
# silvano_sales2 = silvano_sales.replace('ã', 'a')

# print(silvano_sales.replace('çã', 'ca' ))


# strip remove caracteres em branco no final e no inicio de uma string

# jack_stripador = '            removendo espaços de uma string        '

# print(jack_stripador)
# print(jack_stripador.strip())


# split divide uma string em elementos de uma lista

# string_espalhada = 'Paulo Ivo Porto'

# print(string_espalhada)
# print(string_espalhada.split())



# join transforma os elementos de uma lista em uma string
# concatena strings

# nome_lista = ['Paulo', 'Ivo', 'Porto']
# print(' '.join(nome_lista)) 


# slice manipula strig por indice

# cidade = 'Recanto das Emas, cidade do povo'

# print(cidade[::-1])


# Palindromo

# palindromo = 'Arara'

# if palindromo.lower() == palindromo[::-1].lower():
#     print('é palindromo')
# else:
#     print('não é palindromo')





    lista = []

    for in range(10):
        numero = int(input('forneça um número'))
        if numero % 3 == 0:
            lista.append(numero)

    for numero in lista:
        print(numero)






