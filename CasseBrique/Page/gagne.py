import pygame

from p5 import core


class Gagne:
    def __init__(self):
        self.fontBB = pygame.font.Font('Police/BloodBlocks.ttf', 80)

    def YouWin(self):
        Youwin = self.fontBB.render("You Win", True, (255, 255, 255))
        core.screen.blit(Youwin, (150, 500))