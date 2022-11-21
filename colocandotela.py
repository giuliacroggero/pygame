import pygame 

pygame.init()

#colocando tela inicial
WIDTH = 400
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BellyBaloo')

game = True

#colocando imagens
image = pygame.image.load('assets/img/menu.png').convert()
image = pygame.transform.scale(image, (400, 600))
imageplay = pygame.image.load('assets/img/play.png').convert_alpha()
imageplay = pygame.transform.scale(imageplay, (200, 100))
imagefundojogo=pygame.image.load('assets/img/fundojogo.png').convert()
imagefundojogo = pygame.transform.scale(imagefundojogo, (400, 600))

while game:
    window.fill((255, 153, 255))  # Preenche com a cor
    window.blit(image, (0, 0))
    window.blit(imageplay,(100,200))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.blit(imagefundojogo, (0, 0))
    #colocando imagem do play
    
        
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados