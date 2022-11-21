import pygame
import os
from config import MENU_WIDTH, MENU_HEIGHT, BALOO_WIDTH, BALOO_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR

MENU_IMG = 'menu_img'
BALOO_IMG = 'baloo_img'
CANETA_IMG = 'caneta_img'
CONTROLE_IMG = 'controle_img'
LATINHA_IMG = 'latinha_img'
MEIA_IMG = 'meia_img'
RACAO_IMG = 'racao_img'
MACA_IMG = 'maca_img'
BISCOITO_IMG = 'biscoito_img'
CENOURA_IMG = 'cenoura_img'

def load_assets():
    assets = {}
    assets[MENU_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'menu.png')).convert_alpha()
    assets[MENU_IMG] = pygame.transform.scale(assets['menu_img'], (MENU_WIDTH, MENU_HEIGHT))
    assets[BALOO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'baloo.png')).convert_alpha()
    assets[BALOO_IMG] = pygame.transform.scale(assets['baloo_img'], (BALOO_WIDTH, BALOO_HEIGHT))
    assets[CANETA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'caneta.png')).convert_alpha()
    assets[CANETA_IMG] = pygame.transform.scale(assets['caneta_img'], (CANETA_WIDTH, CANETA_HEIGHT))
    assets[CONTROLE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'controle.png')).convert_alpha()
    assets[CONTROLE_IMG] = pygame.transform.scale(assets['controle_img'], (CONTROLE_WIDTH, CONTROLE_HEIGHT))
    assets[LATINHA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'latinha.png')).convert_alpha()
    assets[LATINHA_IMG] = pygame.transform.scale(assets['latinha_img'], (LATINHA_WIDTH, LATINHA_HEIGHT))


    return assets