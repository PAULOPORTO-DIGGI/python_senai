
vencedor = false

import velhas_funcoes as jv

while vencedor ==  False:

    jv.desenhar_tabuleiro()

    jogada = int(input('Onde deseja jogar'))

    jv.jogar(jogada)

    jv.desenhar_tabuleiro()
    jv.troca_jogador()



