import pygame
import os
from config import MENU_WIDTH, MENU_HEIGHT, BALOO_WIDTH, BALOO_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR

MENU_IMG = 'menu_img'
BALOO_IMG = 'baloo_img'

def load_assets():
    assets = {}
    assets[MENU_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'menu.png')).convert_alpha()
    assets[MENU_IMG] = pygame.transform.scale(assets['menu_img'], (MENU_WIDTH, MENU_HEIGHT))
    assets[BALOO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'baloo.png')).convert_alpha()
    assets[BALOO_IMG] = pygame.transform.scale(assets['baloo_img'], (BALOO_WIDTH, BALOO_HEIGHT))

    return assets