import pygame 

pygame.init()

#colocando tela inicial
WIDTH = 400
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BellyBaloo')

game = True

image = pygame.image.load('bla/img/menu.png').convert()
image = pygame.transform.scale(image, (400, 600))

while game:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 153, 255))  # Preenche com a cor
    window.blit(image, (0, 0))

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados