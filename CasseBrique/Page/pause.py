import pygame

from p5 import core


class Pause:
    def __init__(self):
        self.font = pygame.font.Font('Police/Break.ttf', 150)

    def afficher(self, fenetre):
        self.pause = self.font.render("Pause", True, (243, 201, 13))
        core.screen.blit(self.pause, ((fenetre[0]-455)/2, (fenetre[1]-150)/2))
