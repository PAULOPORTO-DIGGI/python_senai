
from os import system
import operacoes as op
# import operacoes
# import operacoes import menu , listar_nomes



operacao = 'sim'



while operacao == 'sim':
    op.menu()
    opcao = int(input('Informe a ação desejada:'))


match opcao:

    case 1:
        nome = input('que nome deseja cadastrar:')
        op.cadastrar_nome(nome)
    case 2:
        nome = input('que nome deseja cadastrar:')
        novo_nome = input( 'Qual será o novo nome?')

        op.atualiza_nome(nome, novo_nome)
    
    case 3:
        nome = input('que nome deseja remover:')
        op.excluir_nome(nome)
    
    case 4:
        op.listar_nomes()

    

    case _:
        print('opcao invalida')


operacao = input('Deseja realizar outra operação?').lower()
system('clear')  

if operacao != 'sim':
    break