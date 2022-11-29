import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'menu.png')).convert()
    background_rect = background.get_rect()
     #play_position = screen #pygame.rect(350, 200, 100, 100)


    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
               # mouse = pygame.mouse.get_pos()
                #if play_position.collidepoint(mouse):
                    state = GAME
                    running=False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state