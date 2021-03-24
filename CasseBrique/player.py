import random

import pygame
from pygame.math import Vector2, Vector3


class Player:
    def __init__(self):
        self.taille = 8
        self.direction = Vector2(0, 0)
        self.position = Vector2(400, 400)
        self.hauteurplayer = 50
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def deplacer(self, position):
        self.position.x = position[0]
        self.position.y = position[1]

    def afficher(self, core, taillex):
        pygame.draw.line(core.screen, self.couleur, (self.position.x-25, taillex-50), (self.position.x+25, taillex-self.hauteurplayer), self.taille)
