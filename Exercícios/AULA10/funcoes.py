
# numero1 = int(input('Informe p numero:'))
# numero2 = int(input('Informe p numero:'))

# print('A soma é: ', numero1 + numero2)

# Metodos estão atrelados ao objeto
# Função 'MAX' acha o maior número



# print(max(numeros)) # Função 'MAX' acha o maior número
# print(min(numeros))
# print(len(numeros)) # Quantidade de numeros
# print(sum(numeros)) #Soma todos os resultados

# media = sum(numeros) / len(numeros)

# print(media)


# Contrução de uma função colocar 'def media() + parametros São odados que podem ser incluidos na função

# numeros = [1, 5, 8, 10, 3, 78, 100, 51]

####RECEBE UM LISTA E CALCULA MÉDIA

# def media (numeros):
#     resultado = sum(numeros) / len(numeros)

#     return resultado

# print(media(numeros))

### FUNÇÃO RECEBE DOIS NÚMEROS E SOMA

# def soma (a , b):
#     soma = a+ b

#### USO DA FUNÇÃO SOMA

#     return soma
# print(soma(15, 35))

### FUNÇÃO SEM RETORNO

# def saudacao(nome):
#     print(f' OLÁ {nome}')


# ## SEM FUNÇÃO
# saudacao('PAULO')

# def ola(nome, mensagem='Olá'):
#     print(mensagem , nome)

# ola('Paulo', 'oi')


### Função com múltiplo retorno



# def dividir (numero1 , numero2):
#     resposta = numero1 // numero2
#     resto = numero1 % numero2

#     return resposta, resto


# divisao, resto_divisao = dividir(9,2)

# print(divisao)
# print(resto_divisao)

### 

## É uma forma de simplificar uma função

# def soma (a,b):
#     soma (a, b)
#     soma = a + b
#     return soma

# somar = lambda a,b: a+ b
# print(somar(10,5))


#### Manda o parametro posicional


# def exibir_informacoes(*args):
#     print('Argumentos posicionais: ' , args)


# exibir_informacoes(1,4 'Paulo', 'Teste')

# def exibir_informacoes2(*args):
#     print('Argumentos posicionais: ' , args)

# exibir_informacoes2(nome=' Luciano', idade =30, curso='python')


# key : value
# chave: valor
### Todo conjunto dicionario

pessoa1 = { ##Objeto (Pessoa)
    'nome': 'luciano', # Chave à esquerda
    'idade': 30,
    'estado_civil': 'casado,' ### Valor à direita depois dos dois pontos (casado)
    'escolaridade': 'especialista'


[},

pessoa2 = { ##Objeto (Pessoa)
    'nome': 'luciano', # Chave à esquerda
    'idade': 30,
    'estado_civil': 'casado,' ### Valor à direita depois dos dois pontos (casado)
    'escolaridade': 'especialista'


[}







