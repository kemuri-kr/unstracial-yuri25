import pygame
import time
import random
def titulo(nome):
    pygame.display.set_caption(nome)
def textador(tela, fonte, tamanho, texto, cor, antilarias, posicao, angulo):
    fon = pygame.font.SysFont(fonte, tamanho)
    textu = fon.render(texto, antilarias, cor)
    textu = pygame.transform.rotate(textu, angulo)
    a = tela.blit(textu, posicao)
    return a

def movimentacao(delay, pos_x, pos_y):
    while True:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            pos_x = pos_x - 5
        if teclas[pygame.K_RIGHT]:
            pos_x = pos_x + 5
        if teclas[pygame.K_UP]:
            pos_y = pos_y - 5
        if teclas[pygame.K_DOWN]:
           pos_y = pos_y + 5
        time.sleep(delay)
