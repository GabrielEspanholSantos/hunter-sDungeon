import numpy as np
import os

clear = lambda: os.system('cls')


def cria_tabuleiro():
    tabuleiro = np.array([
                         ['   ',' A ',' B ',' C ',' D ',' E ',' F ',' G ','   '],
                         [' 1 ',' ! ',' ! ',' O ',' O ',' O ',' ! ',' ! ',' 1 '],
                         [' 2 ',' ! ',' ! ',' O ',' O ',' O ',' ! ',' ! ',' 2 '],
                         [' 3 ',' O ',' O ',' O ',' O ',' O ',' O ',' O ',' 3 '],
                         [' 4 ',' O ',' O ',' O ','   ',' O ',' O ',' O ',' 4 '],
                         [' 5 ',' O ',' O ',' O ',' O ',' O ',' O ',' O ',' 5 '],
                         [' 6 ',' ! ',' ! ',' O ',' O ',' O ',' ! ',' ! ',' 6 '],
                         [' 7 ',' ! ',' ! ',' O ',' O ',' O ',' ! ',' ! ',' 7 '],
                         ['   ',' A ',' B ',' C ',' D ',' E ',' F ',' G ','   ']
                         ])

    return tabuleiro


def printa_tabuleiro(tabuleiro):
    linhas = tabuleiro.shape[0]
    colunas = tabuleiro.shape[1]
    print('\n')
    for i in range(0, linhas):
        print('\t\t        ', end='')
        for j in range(0, colunas):
            print(f'{tabuleiro[i,j]}', end='')
        print('')

    print('\n')


def mostra_instrucoes_entrada():
    print("\t\t---------- INSTRUÇÕES DE ENTRADA ----------\n \
\tPara indicar uma posição no tabuleiro utilize a notação\n \
\t'letra_coluna numero_linha', deixando apenas um espaço\n \
\tentre o número da linha e a letra da coluna.\n\n")


def solicita_jogada(tabuleiro):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    while True:
        try:  #? Verificação da posição da peça
            peca = input('\tIndique a letra da coluna e o número da linha da peça que deseja mover: ').split(' ')
            if ''.join(peca).lower() == 'x':
                quit()
            elif ''.join(peca).lower() == 'm':
                return ''.join(peca).lower()
                break
            
            col_peca = peca[0].upper()
            if col_peca in letras:  #? Verificação da letra onde se encontra a peça do jogador
                pass
            else:
                clear()
                print('\tDigite uma letra válida (A a G) para a coluna\n')
                mostra_instrucoes_entrada()
                printa_tabuleiro(tabuleiro)
                continue

            try:  #? Verificação da linha onde se encontra a peça do jogador
                lin_peca = int(peca[1])
                if lin_peca > 0 and lin_peca < 8:
                    break
                else:
                    clear()
                    print('\tDigite um valor válido (1 a 7) para o número da linha\n')
                    mostra_instrucoes_entrada()
                    printa_tabuleiro(tabuleiro)
                    continue

            except ValueError:
                clear()
                print('\tDigite um valor inteiro para o número da linha\n')
                mostra_instrucoes_entrada()
                printa_tabuleiro(tabuleiro)
                continue
            
        except IndexError:
            clear()
            print('\tSua entrada não corresponde com a especificada nas instruções, por favor, digite novamente:\n')
            mostra_instrucoes_entrada()
            printa_tabuleiro(tabuleiro)
            continue

    while True:
        try:  #? Verificação do movimento
            mov = input('\tIndique a letra da coluna e o número da linha para onde deseja mover esta peça: ').split(' ')
            if ''.join(mov).lower() == 'x':
                quit()
            elif ''.join(mov).lower() == 'm':
                return ''.join(mov).lower()
                break

            col_mov = mov[0].upper()
            if col_mov in letras: #? Verificação da letra para onde o jogador deseja mover a peça
                pass
            else:
                clear()
                print('\tDigite uma letra válida (A a G) para a coluna\n')
                mostra_instrucoes_entrada()
                printa_tabuleiro(tabuleiro)
                continue

            try: #? Verificação da linha para onde o jogador deseja mover a peça
                lin_mov = int(mov[1])
                if lin_mov > 0 and lin_mov < 8:
                    break
                else:
                    clear()
                    print('\tDigite um valor válido (1 a 7) para o número da linha\n')
                    mostra_instrucoes_entrada()
                    printa_tabuleiro(tabuleiro)
                    continue

            except ValueError:
                clear()
                print('\tDigite um valor inteiro para o número da linha\n')
                mostra_instrucoes_entrada()
                printa_tabuleiro(tabuleiro)
                continue

            
        except IndexError:
            clear()
            print('\tSua entrada não corresponde com a especificada nas instruções, por favor, digite novamente:\n')
            mostra_instrucoes_entrada()
            printa_tabuleiro(tabuleiro)
            continue
    
    return lin_peca, col_peca, lin_mov, col_mov


def movimenta_peca():
    letras_mov = {
                  'A':1,
                  'B':2,
                  'C':3,
                  'D':4,
                  'E':5,
                  'F':6,
                  'G':7
                 }

    tabuleiro = cria_tabuleiro()
    printa_tabuleiro(tabuleiro)
    tabuleiro_atual = tabuleiro
    tabuleiro_anterior = tabuleiro
    
    while True:
        if tabuleiro_atual is not 0:
            fim_de_jogo = verifica_fim_de_jogo(tabuleiro)

            if fim_de_jogo[0] and fim_de_jogo[1] == 1:
                printa_tabuleiro(tabuleiro_atual)
                print("\tParabéns, você venceu!!!\n")
                input("\tPressione qualquer tecla para voltar ao menu")
                break
            elif fim_de_jogo[0] and fim_de_jogo[1] == 0:
                printa_tabuleiro(tabuleiro_atual)
                print("\tInfelizmente não existem mais jogadas possíveis.")
                input("\tPressione qualquer tecla para voltar ao menu")
                break
            else:
                clear()
                printa_tabuleiro(tabuleiro_atual)
                posicoes = solicita_jogada(tabuleiro_atual)

                if posicoes == 'm':
                    break

                pos_peca = [posicoes[0], letras_mov[posicoes[1]]]
                pos_mov = [posicoes[2], letras_mov[posicoes[3]]]

                tabuleiro_anterior = np.copy(tabuleiro_atual)
                tabuleiro_atual = verifica_movimento(tabuleiro, pos_peca, pos_mov)

        elif tabuleiro_anterior is not 0:
            clear()
            print('\n\t\tMovimento inválido, insira novamnete: ')
            tabuleiro_atual = tabuleiro_anterior
            printa_tabuleiro(tabuleiro_atual)

            posicoes = solicita_jogada(tabuleiro_atual)

            if posicoes == 'm':
                break

            pos_peca = [posicoes[0], letras_mov[posicoes[1]]]
            pos_mov = [posicoes[2], letras_mov[posicoes[3]]]

            tabuleiro_anterior = np.copy(tabuleiro_atual)
            tabuleiro_atual = verifica_movimento(tabuleiro, pos_peca, pos_mov)
            continue


def verifica_movimento(tabuleiro, peca, mov):
    mov_valido = False

    largura_movimento_linha = peca[0] - mov[0]
    largura_movimento_coluna = peca[1] - mov[1]
    
    if (abs(largura_movimento_linha) == 2 and largura_movimento_coluna == 0):
        if tabuleiro[peca[0], peca[1]] == ' O ' and tabuleiro[mov[0], mov[1]] == '   ':
            if largura_movimento_linha < 0:
                y_axis = -1
                x_axis = 0
            else:
                y_axis = 1
                x_axis = 0

            captura = [mov[0] + y_axis, mov[1] + x_axis]
            if tabuleiro[captura[0], captura[1]] == ' O ':
                mov_valido = True

    elif (largura_movimento_linha == 0 and abs(largura_movimento_coluna) == 2):
        if tabuleiro[peca[0], peca[1]] == ' O ' and tabuleiro[mov[0], mov[1]] == '   ':
            if largura_movimento_coluna < 0:
                x_axis = -1
                y_axis = 0
            else:
                x_axis = 1
                y_axis = 0

            captura = [mov[0] + y_axis, mov[1] + x_axis]
            if tabuleiro[captura[0], captura[1]] == ' O ':
                mov_valido = True
    

    if mov_valido:
        tabuleiro[mov[0], mov[1]] = ' O '
        tabuleiro[peca[0], peca[1]] = '   '
        tabuleiro[captura[0], captura[1]] = '   '
    else:
        return 0

    return tabuleiro


def verifica_fim_de_jogo(tabuleiro):
    linhas = tabuleiro.shape[0]
    colunas = tabuleiro.shape[1]

    pecas_restantes = 0
    posicoes_peca = []
    for i in range(1, linhas-1):
        for j in range(1, colunas-1):
            if tabuleiro[i,j] == ' O ':
                pecas_restantes += 1
                posicoes_peca.append((i,j))

    mov_possivel = False
    if pecas_restantes > 1:

        posicoes_peca_linha = sorted(posicoes_peca)
        lin = posicoes_peca_linha[0][0]
        col = posicoes_peca_linha[0][1]
        for pos in posicoes_peca_linha[1:]:
            if (lin == pos[0] and abs(col - pos[1]) == 1):
                if tabuleiro[pos[0], pos[1]+1] == '   ' or tabuleiro[lin, col-1] == '   ':
                    mov_possivel = True
                    break
            lin = pos[0]
            col = pos[1]
        
        posicoes_peca_coluna = sorted(posicoes_peca, key=retorna_segundo_elemento)
        lin = posicoes_peca_coluna[0][0]
        col = posicoes_peca_coluna[0][1]
        for pos in posicoes_peca_coluna:
            if col == pos[1] and abs(lin - pos[0]) == 1:
                if tabuleiro[pos[0]+1, pos[1]] == '   ' or tabuleiro[lin-1, col] == '   ':
                    mov_possivel = True
                    break
            lin = pos[0]
            col = pos[1]

    else:
        return (True, 1)
    
    if mov_possivel:
        return (False, 0)
    else:
        return (True, 0)
    

def retorna_segundo_elemento(elem):
    return elem[1]
    

def mostra_instrucoes_jogo():
    print('\n\n\t\t\t------------ BEM VINDO AO JOGO RESTA UM ------------\n\n')
    print("\t\t\t----------------- INSTRUÇÕES DO JOGO -----------------\n \
\t- Objetivo: O Objetivo do jogo é fazer com que reste apenas uma peça no tabuleiro.\n \
\t- Os movimentos podem ser feitos pulando por cima das peças, apenas uma casa por vez.\n \
\t- Ao pular uma peça você a retira do jogo (captura).\n \
\t- Caso sobrem duas ou mais peças de forma que não seja possível capturá-las você perde o jogo.\n \
\t- Os espaços no tabuleiro demarcados com um simbolo de exclamação são inválidos para movimento,\n \
\t- Espaços em branco no tabuleiro são espaços válidos para movimento.\n \
\t- As peças são representadas pela letra O.\n \
\t- Pressione a tecla 'x' a qualquer momento durante o jogo para sair e 'm' para voltar ao menu.\n\n")

    input("\t Pressione enter para voltar ao menu")

    
def start():
    while True:
        clear()
        print('\n\n\t\t-------- BEM VINDO AO JOGO RESTA UM --------\n\n')
        print('\t1 -> Jogar')
        print('\t2 -> Instruções do jogo')
        print('\t3 -> Sair do jogo')
        resp = int(input('\t-> '))
        print('\n')
        
        if resp == 1:
            mostra_instrucoes_entrada()
            movimenta_peca()
        elif resp == 2:
            mostra_instrucoes_jogo()
        else:
            quit()

start()