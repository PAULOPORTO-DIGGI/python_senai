



# cavaleiros = ['Seya', 'Shun', 'Shiryu', 'Yoga']

# print(cavaleiros)

# # '.append' adiciona um novo elemento no final da lista
# cavaleiros.append('IKKi')

# print(cavaleiros)
# # '.extend' extentendo a lista com novos nomes
# cavaleiros.extend(['China', 'Maryn'])
# print(cavaleiros)

# # 'insert' inserir em qualquer parte da lista
# cavaleiros.insert(0,'Atena')
# print(cavaleiros)

# # 'remove' exclui o elemento pelo valor.

# cavaleiros.remove('Shun')
# print(cavaleiros)

# # pop - exclui o último elemento da lista ou o indice informado excluiu a 'Marin'

# # elemento = cavaleiros.pop() # Mostra o elemento excluído
# # cavaleiros.pop()
# # print(cavaleiros)

# # print(elemento)


# # Metodo está sempre vinculado ao um objeto a que pertence
# # Indice - retorna o indice da primeira ocorrência de um valor procurado

# print(cavaleiros.index('Yoga'))

# cavaleiros.pop(cavaleiros.pop(cavaleiros.index('Yoga'))

# print(cavaleiros)

# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
# # Contabilizando quantidade de elementos repetidos
# print(cavaleiros.count('Aldebaran'))

# # 'sort' ordena a lista de forma crescente
## 'reverese' ordena a lista de forma decrescente

#CTRL + SHIFT + HOME SELECIONA TUDO PARA TRÁS

frutas = ['morango', 'maça', 'abacaxi', 'Kiwi', 'amora', 'umbu', 'laranja', 'bergamota']
numeros = [ 9, 5, 81, 100, 33, 21, 2]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

frutas.reverse()
numeros.reverse()
print(frutas)
print(numeros)

del frutas[0]
print(frutas)

frutas.clear()
print(frutas)






