import random

import pygame
from pygame.math import Vector2, Vector3


class Brique:
    def __init__(self, x, y):
        self.val = random.choice([0, 5, 10, 20, 30])

        if 1 <= self.val < 8:
            color = Vector3(0, 255, 0)
        elif 8 <= self.val < 15:
            color = Vector3(255, 255, 0)
        elif 15 <= self.val < 25:
            color = Vector3(255, 125, 0)
        elif 25 <= self.val < 31:
            color = Vector3(255, 0, 0)
        else:
            color = Vector3(0, 0, 0)

        self.couleur = color

        self.position = Vector2(x, y)

    def afficher(self, core):

        if 1 <= self.val < 8:
            color = Vector3(0, 255, 0)
        elif 8 <= self.val < 15:
            color = Vector3(255, 255, 0)
        elif 15 <= self.val < 25:
            color = Vector3(255, 125, 0)
        elif 25 <= self.val < 31:
            color = Vector3(255, 0, 0)
        else:
            color = Vector3(0, 0, 0)

        self.couleur = color

        if self.val != 0:
            pygame.draw.rect(core.screen, self.couleur, (self.position.x, self.position.y, 35, 35))

