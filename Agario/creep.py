import random

import pygame
from pygame.math import Vector2, Vector3


class Creep:
    def __init__(self, largeur, hauteur):
        self.taille = 2
        self.position = Vector2(random.randint(0,largeur), random.randint(0,hauteur))
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def mourir(self):
        pass

    def afficher(self, core):
        pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)),
                           (int(self.position.x), int(self.position.y)), self.taille)

