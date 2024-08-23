### 45. Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

from socket import NI_NUMERICHOST


# maior = 0

# for i in range(5):

#     numero = int(input(f'Informe o nuerero {i + 1} \n'))

# if numero > maior:
#     maior = numero

#     print(f'O maior numero é: {maior}')

maior = 0

for i in range(5):

    numero = int(input(f'Informe o nuerero {i + 1} \n'))

if numero > maior:
    maior = numero

    print(f'O maior numero é: {maior}')

    
