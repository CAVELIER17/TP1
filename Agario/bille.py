import random

from pygame.math import Vector2, Vector3


class Bille:
    def __init__(self):
        self.taille = 1
        self.direction = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def manger(self):
        pass

    def mourir(self):
        pass

    def suivre(self):
        pass

    def afficher(self):
        pass
