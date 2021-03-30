import sys, math, random, pygame
from pygame.constants import K_f, K_p

from p5 import core


def setup():
    print("Setup START---------")
    # Initialisation fenetre
    core.fps = 90
    core.WINDOW_SIZE = [800, 800]
    core.TITLE_WINDOW = "test"


def run():
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text0 = my_font.render("Choose the mode you want", True, (255, 255, 255))
    core.screen.blit(text0, (200, 200))



if __name__ == '__main__':
    core.main(setup, run)
