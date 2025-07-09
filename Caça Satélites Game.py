import random

linhas = colunas = 6

matriz = []

for i in range (linhas):
    linha = []
    for j in range (colunas):
        linha.append(0)
    matriz.append(linha)

contador = 0

while contador < 4:
    i = random.randint(0, linhas - 1)
    j = random.randint(0, colunas - 1)

    if matriz[i][j] == 0:
        matriz[i][j] = 1
        contador += 1

matriz_sobreposta = []

for linha in range (6):
    matriz_dois = []
    for coluna in range(6):
        matriz_dois.append('?')
    matriz_sobreposta.append(matriz_dois)

#inicio_jogo
print("""Neste jogo, você é a comandante de uma base de defesa orbital da Terra. Satélites espiões 
foram lançados por uma nação inimiga e estão escondidos na órbita terrestre.
      
Sua missão é identificar e desativar todos os satélites antes que eles
transmitam informações sigilosas.""")

input("\033[1:034mAPERTE ENTER PARA LER AS REGRAS DO JOGO...\033[m")

print("""Neste jogo, o espaço orbital é representado por uma matriz 6x6. O computador posiciona
aleatoriamente 4 satélites espiões (1) em setores distintos, enquanto os demais
permanecem como espaço vazio (0). 
      
A cada rodada, você escolhe uma coordenada (linha e coluna) para lançar um feixe de interferência. 
Se houver um satélite na posição escolhida, ele será desativado e a célula marcada com -1. 
O jogo continua até que todos os 4 satélites sejam encontrados.
      
Após cada tentativa, o programa exibe uma versão oculta da matriz, com as seguintes
representações:
● X para satélites desativados (-1),
● . (ponto) para posições escaneadas onde não havia satélite,
● ? (interrogação) para posições ainda não verificadas.""")

input("\033[1:034mAPERTE ENTER PARA COMEÇAR!\033[m")

#mecanica do laser
contador_tentativas = 0
contador_naves = 0

for linha_sobreposta in matriz_sobreposta:
    print(' '.join(f'{s:^3}' for s in linha_sobreposta))

while contador_naves < 4:
    try:
        print(f'Rodada {contador_tentativas + 1}'.center(23))

        x = int(input(f'Digite uma linha (0:5): '))
        while x > 5 or x < 0:
            print('Linha inválida ❌')
            x = int(input(f'Digite uma outra linha (0:5): '))

        y = int(input(f'Digite uma coluna (0:5): '))
        while y > 5 or x < 0:
            print('Coluna inválida ❌')
            y = int(input(f'Digite uma outra coluna (0:5): '))

        if matriz_sobreposta[x][y] == "?":

            if matriz[x][y] == 1: #atingir
                contador_naves += 1
                restantes = 4 - contador_naves
                print(f'\033[32mALVO ATINGIDO! RESTAM {restantes}\033[0m'.center(23))
                matriz[x][y] = -1
                matriz_sobreposta[x][y] = "X"
                for linha_sobreposta in matriz_sobreposta:
                    print(' '.join(f'{s:^3}' for s in linha_sobreposta))

            else: #não atingir
                print('\033[91mNENHUM ALVO ATINGIDO\033[0m'.center(23))
                matriz_sobreposta[x][y] = "."
                for linha_sobreposta in matriz_sobreposta:
                    print(' '.join(f'{s:^3}' for s in linha_sobreposta))
            contador_tentativas += 1
        
        else:
            print('\033[91mCOORDENADA JÁ UTILIZADA!\033[0m'.center(23))
            for linha_sobreposta in matriz_sobreposta:
                print(' '.join(f'{s:^3}' for s in linha_sobreposta))

    except ValueError:
        print('\033[91mErro!\033[0m')

if contador_naves == 4:
    print(f'\033[32mPARABÉNS! VOCÊ ZEROU EM {contador_tentativas} RODADAS!\033[0m'.center(23))

input('Aperte ENTER para sair!')