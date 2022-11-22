import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import load_assets, SCORE_FONT
from sprites import baloo, comidas, objetos



def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando grupos
    all_sprites = pygame.sprite.Group()
    all_objetos = pygame.sprite.Group()
    all_comidas = pygame.sprite.Group()
    #all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_objetos'] = all_objetos
    groups['all_comidas'] = all_comidas

    # Criando o jogador
    player = baloo(groups, assets)
    all_sprites.add(player)
    # Criando os objetos
    for i in range(3):
        Objetos = objetos(assets)
        all_sprites.add(objetos)
        all_comidas.add(objetos)
    for i in range(4):
        Comidas = comidas(assets)
        all_sprites.add(comidas)
        all_comidas.add(comidas)

    DONE = 0
    PLAYING = 1
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre baloo e objeto
            hits = pygame.sprite.spritecollide(player, all_objetos, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                #toca o latido e são criados novos objetos
                assets['procurar som de reclamacao'].play()
                o = objetos(assets)
                all_sprites.add(o)
                all_objetos.add(o)
                lives =  lives - 1

                score = score
                #Fazer sumir o objeto que encostou no baloo

        if lives == 0:
                state = DONE
        else:
            state = PLAYING
            player = baloo(groups, assets)
            all_sprites.add(player)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        #window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
    
        # Desenhando o score
        #text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
