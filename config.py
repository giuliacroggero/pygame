from os import path

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 400 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60
MENU_WIDTH = 400
MENU_HEIGHT = 600
BALOO_WIDTH = 40
BALOO_HEIGHT = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


INIT = 0
GAME = 1
QUIT = 2