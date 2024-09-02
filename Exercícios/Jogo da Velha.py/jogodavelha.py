from os import system

tabuleiro = [0,1,2,3,4,5,6,7,8]

jogador = 'x'

def desenhar_tabuleiro():
    for i in enumerate(tabuleiro):
     if i == 2 or i == 5:
        print(i)
    print(i)


    for i in tabuleiro:
        if i == 2 or i == 5:
          
            print(i)
        else:
            print(i, end='')
def jogar(jogada):
    tabuleiro[jogada] = jogador

def troca_jogador():
    if jogador == 'X':
        jogador == 'O'
    else:
        jogador == 'X'
