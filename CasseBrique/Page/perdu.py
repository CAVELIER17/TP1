import pygame

from p5 import core


class Perdu:
    def __init__(self):
        self.fontBB = pygame.font.Font('Police/BloodBlocks.ttf', 150)

    def GameOver(self, fenetre):
        self.gameover = self.fontBB.render("Game Over", True, (255, 255, 255))
        core.screen.blit(self.gameover, ((fenetre[0]-594)/2, (fenetre[1]-150)/2))