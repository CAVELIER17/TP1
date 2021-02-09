from pygame.math import Vector2, Vector3


class Player:
    def __init__(self):
        self.taille = 1
        self.vitesse = 2
        self.forme = "circle"
        self.direction = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.couleur = Vector3(255, 0, 0)

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self):
        pass

    def afficher(self):
        pass
