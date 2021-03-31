import pygame

from p5 import core


class Gagne:
    def __init__(self):
        self.fontBB = pygame.font.Font('Police/KissBoom.ttf', 150)

    def YouWin(self, fenetre):
        self.Youwin = self.fontBB.render("You Win", True, (243, 201, 13))
        core.screen.blit(self.Youwin, ((fenetre[0]-594)/2, (fenetre[1]-130)/2))
