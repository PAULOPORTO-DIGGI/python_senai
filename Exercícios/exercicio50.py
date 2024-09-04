texto1 = 'Luciano lopes'

def saudacao():
    print(f'Olá {texto1} - esse texto veio da função')
    texto2 = 'Tia Fran'
    print(f'olá {texto2} - esse texto veio da função')

saudacao()
print(f'Olá {texto1} - esse texto veio de fora da função')
print(f'Olá {texto2} - esse texto veio de fora da função')

