import random
import pygame
from config import WIDTH, HEIGHT, CANETA_WIDTH, CANETA_HEIGHT, CONTROLE_WIDTH, CONTROLE_HEIGHT, LATINHA_WIDTH, LATINHA_HEIGHT, MACA_WIDTH, CENOURA_WIDTH, RACAO_WIDTH, BISCOITO_WIDTH, MACA_HEIGHT, CENOURA_HEIGHT, RACAO_HEIGHT, BISCOITO_HEIGHT
from assets import BALOO_IMG, CANETA_IMG, CONTROLE_IMG, LATINHA_IMG, MACA_IMG, RACAO_IMG, CENOURA_IMG, BISCOITO_IMG


class baloo(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BALOO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        # Atualização da posição do baloo
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    '''def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_bullets'].add(new_bullet)
            #self.assets[BLA_SOUNDS].play()'''

class objetos(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CANETA_IMG]
        self.image = assets[CONTROLE_IMG]
        self.image = assets[LATINHA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-CANETA_WIDTH, CONTROLE_WIDTH, LATINHA_WIDTH)
        self.rect.y = random.randint(-100, -CANETA_HEIGHT, CONTROLE_HEIGHT, LATINHA_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do objetos
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o objeto passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-CANETA_WIDTH, CONTROLE_WIDTH, LATINHA_WIDTH)
            self.rect.y = random.randint(-100, -CANETA_HEIGHT, CONTROLE_HEIGHT, LATINHA_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

class comidas(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MACA_IMG]
        self.image = assets[CENOURA_IMG]
        self.image = assets[RACAO_IMG]
        self.image = assets[BISCOITO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-MACA_WIDTH, CENOURA_WIDTH, RACAO_WIDTH, BISCOITO_WIDTH)
        self.rect.y = random.randint(-100, -MACA_HEIGHT, CENOURA_HEIGHT, RACAO_HEIGHT, BISCOITO_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-MACA_WIDTH, CENOURA_WIDTH, RACAO_WIDTH, BISCOITO_WIDTH)
            self.rect.y = random.randint(-100, -MACA_HEIGHT, CENOURA_HEIGHT, RACAO_HEIGHT, BISCOITO_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)
    

