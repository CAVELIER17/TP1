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
    player1 = Player((fen_x, fen_y))
    bille1 = Bille()
    for i in range(0, 22):
        for j in range(0, 8):
            briques.append(Brique(i * entraxeB, j * entraxeB))


def run():
    for b in briques:
        b.afficher(core)

    if bille1.start:

        player1.afficher(core)
        bille1.afficher(core)

        player1.deplacer(pygame.mouse.get_pos())
        bille1.deplacer((bille1.position.x - bille1.direction.x, bille1.position.y + bille1.direction.y))

        #
        for t in briques:
            if t.val <= 0:
                briques.remove(t)
            if t.position.x-4 < bille1.position.x < t.position.x + entraxeB+4 and t.position.y-4 < bille1.position.y < t.position.y + entraxeB+4:
                bille1.direction.y = -bille1.direction.y
                t.val = t.val - 30

        # Rebond droite/gauche
        if not bille1.taille <= bille1.position.x <= fen_x - bille1.taille:
            bille1.direction.x = -bille1.direction.x

        # Rebond plafond
        if (bille1.position.y - bille1.taille)<=0:
            bille1.direction.y = -bille1.direction.y

        # Rebond table
        if (bille1.position.y + bille1.taille) >= (fen_y - (
                player1.taille / 2) - player1.hauteurplayer) and player1.position.x - player1.largeur <= bille1.position.x <= player1.position.x + player1.largeur:
            bille1.direction.y = -bille1.direction.y

    else:
        player1.afficher(core)
        bille1.deplacer((fen_x / 2, player1.position.y - player1.hauteurplayer - (player1.taille / 2) - bille1.taille))
        bille1.afficher(core)

        if core.getMouseLeftClick():
            bille1.direction.x = 4#(bille1.position.x - pygame.mouse.get_pos()[0]) / 15
            bille1.direction.y = -8#(bille1.position.x - pygame.mouse.get_pos()[1]) / 15
            #pygame.mouse.set_pos(player1.position)
            bille1.start = True


if __name__ == '__main__':
    core.main(setup, run)
