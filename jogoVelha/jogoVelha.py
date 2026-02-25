
import pygame
import sys
pygame.init()
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
TAMANHO = 300
LINHA = 100
LARGURA_LINHA = 10
RAIO = 30
LARGURA_CIRCULO = 10
LARGURA_X = 15
ESPACO = 25
tela = pygame.display.set_mode((TAMANHO, TAMANHO))
pygame.display.set_caption('Jogo da Velha')

tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
jogador = 1
fim_de_jogo = False
menu = True
menu_fim = False
vencedor = None
empate = False

def desenhar_linhas():
    for i in range(1, 3):
        pygame.draw.line(tela, PRETO, (0, i * LINHA), (TAMANHO, i * LINHA), LARGURA_LINHA)
        pygame.draw.line(tela, PRETO, (i * LINHA, 0), (i * LINHA, TAMANHO), LARGURA_LINHA)

def desenhar_figuras():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 1:
                pygame.draw.circle(tela, AZUL, (coluna * LINHA + LINHA // 2, linha * LINHA + LINHA // 2), RAIO, LARGURA_CIRCULO)
            elif tabuleiro[linha][coluna] == 2:
                x = coluna * LINHA
                y = linha * LINHA
                pygame.draw.line(tela, VERMELHO, (x + ESPACO, y + ESPACO), (x + LINHA - ESPACO, y + LINHA - ESPACO), LARGURA_X)
                pygame.draw.line(tela, VERMELHO, (x + ESPACO, y + LINHA - ESPACO), (x + LINHA - ESPACO, y + ESPACO), LARGURA_X)

def checar_vitoria(jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    for col in range(3):
        if [tabuleiro[linha][col] for linha in range(3)].count(jogador) == 3:
            return True
    if [tabuleiro[i][i] for i in range(3)].count(jogador) == 3:
        return True
    if [tabuleiro[i][2 - i] for i in range(3)].count(jogador) == 3:
        return True
    return False

def checar_empate():
    for linha in tabuleiro:
        if 0 in linha:
            return False
    return True

def reiniciar():
    global tabuleiro, jogador, fim_de_jogo, menu, menu_fim, vencedor, empate
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    jogador = 1
    fim_de_jogo = False
    menu = True
    menu_fim = False
    vencedor = None
    empate = False

def main():
    global jogador, fim_de_jogo, menu, menu_fim, vencedor, empate
    tela.fill(BRANCO)
    desenhar_linhas()
    fonte = pygame.font.SysFont(None, 40)
    fonte_menu = pygame.font.SysFont(None, 32)
    clock = pygame.time.Clock()
    while True:
        if menu:
            tela.fill(BRANCO)
            msg1 = fonte_menu.render('Jogo da Velha', True, PRETO)
            msg2 = fonte_menu.render('Pressione 1 para Jogador 1', True, AZUL)
            msg3 = fonte_menu.render('Pressione 2 para Jogador 2', True, VERMELHO)
            tela.blit(msg1, (TAMANHO//2 - msg1.get_width()//2, 40))
            tela.blit(msg2, (TAMANHO//2 - msg2.get_width()//2, 100))
            tela.blit(msg3, (TAMANHO//2 - msg3.get_width()//2, 140))
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        jogador = 1
                        menu = False
                    elif evento.key == pygame.K_2:
                        jogador = 2
                        menu = False
            clock.tick(30)
            continue
        if menu_fim:
            tela.fill(BRANCO)
            desenhar_linhas()
            desenhar_figuras()
            if vencedor:
                texto = f'Jogador {vencedor} venceu!'
            elif empate:
                texto = 'Empate!'
            else:
                texto = ''
            if texto:
                msg = fonte.render(texto, True, (0, 128, 0))
                tela.blit(msg, (TAMANHO//2 - msg.get_width()//2, 60))
            msg4 = fonte_menu.render('Pressione R para jogar novamente', True, PRETO)
            msg5 = fonte_menu.render('Pressione Q para sair', True, PRETO)
            tela.blit(msg4, (TAMANHO//2 - msg4.get_width()//2, 120))
            tela.blit(msg5, (TAMANHO//2 - msg5.get_width()//2, 160))
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        reiniciar()
                    elif evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            clock.tick(30)
            continue
        # Tela do jogo
        tela.fill(BRANCO)
        desenhar_linhas()
        desenhar_figuras()
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and not fim_de_jogo:
                x, y = evento.pos
                linha = y // LINHA
                coluna = x // LINHA
                if tabuleiro[linha][coluna] == 0:
                    tabuleiro[linha][coluna] = jogador
                    if checar_vitoria(jogador):
                        fim_de_jogo = True
                        vencedor = jogador
                        menu_fim = True
                    elif checar_empate():
                        fim_de_jogo = True
                        empate = True
                        menu_fim = True
                    else:
                        jogador = 2 if jogador == 1 else 1
        clock.tick(30)

if __name__ == '__main__':
    main()
