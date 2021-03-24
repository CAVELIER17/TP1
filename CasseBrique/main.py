import pygame

from p5 import core
from CasseBrique.player import Player
from CasseBrique.brique import Brique
from CasseBrique.bille import Bille

# Initialisation Variable
briques = []
player1 = None
bille1 = None
fen_x = 770
fen_y = 800
entraxeB = 35


def setup():
    print("Setup START---------")
    # Initialisation fenetre
    core.fps = 30
    core.WINDOW_SIZE = [fen_x, fen_y]
    core.TITLE_WINDOW = "Casse Brique"

    # Initialisation Variable
    global player1
    global bille1

    # Création player, bille, briques
    player1 = Player()
    bille1 = Bille()
    for i in range(0, 22):
        for j in range(0, 8):
            briques.append(Brique(i * 35, j * 35))



def run():
    # print("Run")
    player1.afficher(core, fen_y)

    for b in briques:
        b.afficher(core)

    bille1.afficher(core, pygame.mouse.get_pos())
    player1.deplacer(pygame.mouse.get_pos())
    for t in briques:
        if t.position.x < bille1.position.x < t.position.x + entraxeB and t.position.y < bille1.position.y - (
                bille1.taille + 1) < t.position.y + entraxeB:
            t.val = t.val - 1


if __name__ == '__main__':
    core.main(setup, run)
