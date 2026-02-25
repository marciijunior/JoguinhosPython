# Jogo da Cobrinha em Python
# Utilizaremos a biblioteca pygame para facilitar o desenvolvimento

import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Definições de cores
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERDE_ESCURO = (0, 120, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# Tamanho da tela
LARGURA = 600
ALTURA = 400
TAMANHO_BLOCO = 20

# Configuração da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Cobrinha')

# Função para desenhar a cobrinha
def desenhar_cobrinha(tamanho, lista_cobra):
    total = len(lista_cobra)
    for i, x in enumerate(lista_cobra):
        # Gradiente do corpo: do verde claro (cauda) ao verde escuro (cabeça)
        if total > 1:
            fator = i / (total - 1)
        else:
            fator = 1
        r = int(VERDE[0] * (1 - fator) + VERDE_ESCURO[0] * fator)
        g = int(VERDE[1] * (1 - fator) + VERDE_ESCURO[1] * fator)
        b = int(VERDE[2] * (1 - fator) + VERDE_ESCURO[2] * fator)
        cor_gradiente = (r, g, b)
        if i == len(lista_cobra) - 1:
            # Cabeça da cobra (oval)
            pygame.draw.ellipse(tela, cor_gradiente, [x[0], x[1], TAMANHO_BLOCO, TAMANHO_BLOCO])
            # Olhos
            olho_tam = tamanho // 5
            pygame.draw.circle(tela, BRANCO, (x[0] + olho_tam*2, x[1] + olho_tam), olho_tam)
            pygame.draw.circle(tela, BRANCO, (x[0] + olho_tam*2, x[1] + tamanho - olho_tam), olho_tam)
            pygame.draw.circle(tela, PRETO, (x[0] + olho_tam*2, x[1] + olho_tam), olho_tam//2)
            pygame.draw.circle(tela, PRETO, (x[0] + olho_tam*2, x[1] + tamanho - olho_tam), olho_tam//2)
        else:
            # Corpo da cobra (retângulo)
            pygame.draw.rect(tela, cor_gradiente, [x[0], x[1], TAMANHO_BLOCO, TAMANHO_BLOCO], border_radius=6)

# Função principal
def desenhar_grade():
    # Desenha linhas verticais
    for x in range(0, LARGURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, ALTURA))
    # Desenha linhas horizontais
    for y in range(0, ALTURA, TAMANHO_BLOCO):
        pygame.draw.line(tela, (40, 40, 40), (0, y), (LARGURA, y))

def jogo():
    fim_de_jogo = False
    sair = False

    x = LARGURA // 2
    y = ALTURA // 2
    x_mudanca = 0
    y_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 35)

    while not sair:
        while fim_de_jogo:
            tela.fill(PRETO)
            mensagem = fonte.render('Fim de jogo! Pressione Q para sair ou C para jogar novamente', True, BRANCO)
            tela.blit(mensagem, [LARGURA // 10, ALTURA // 2])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sair = True
                    fim_de_jogo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        sair = True
                        fim_de_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_mudanca == 0:
                    x_mudanca = -TAMANHO_BLOCO
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x_mudanca == 0:
                    x_mudanca = TAMANHO_BLOCO
                    y_mudanca = 0
                elif evento.key == pygame.K_UP and y_mudanca == 0:
                    y_mudanca = -TAMANHO_BLOCO
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN and y_mudanca == 0:
                    y_mudanca = TAMANHO_BLOCO
                    x_mudanca = 0

        if x >= LARGURA or x < 0 or y >= ALTURA or y < 0:
            fim_de_jogo = True

        x += x_mudanca
        y += y_mudanca

        tela.fill(PRETO)
        desenhar_grade()
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_de_jogo = True

        desenhar_cobrinha(TAMANHO_BLOCO, lista_cobra)
        texto_pontos = fonte.render(f'Pontos: {comprimento_cobra - 1}', True, BRANCO)
        tela.blit(texto_pontos, [0, 0])
        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comprimento_cobra += 1

        relogio.tick(8)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    jogo()
