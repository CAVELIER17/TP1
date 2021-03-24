import random

import pygame
from pygame.math import Vector2, Vector3


class Bille:
    def __init__(self):
        self.taille = 6
        self.direction = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.start = False

    def afficher(self, core, position):
        self.position = Vector2(position)
        pygame.draw.circle(core.screen, self.couleur, position, self.taille)
