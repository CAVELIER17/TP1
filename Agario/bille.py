from pygame.math import Vector2, Vector3


class Bille:
    def __init__(self):
        self.taille = 1
        self.vitesse = 2
        self.direction = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.couleur = Vector3(0, 255, 0)

    def manger(self):
        pass

    def mourir(self):
        pass

    def suivre(self):
        pass

    def afficher(self):
        pass
