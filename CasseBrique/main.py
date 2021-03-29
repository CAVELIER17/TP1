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
demarrage = False
pause = False
fronMTPause = None


def setup():
    print("Setup START---------")
    # Initialisation fenetre
    core.fps = 90
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
    global demarrage
    global pause
    global fronMTPause


    for b in briques:
        b.afficher(core)

    if demarrage:

        player1.afficher(core)
        bille1.afficher(core)

        bille1.deplacer((bille1.position.x - bille1.direction.x, bille1.position.y + bille1.direction.y))

        #Mode Pause
        if core.getkeyPress():
            if core.getkeyPressValue() == fronMTPause and fronMTPause != 112:
                    pause = not pause
                    fronMTPause = core.getkeyPressValue()


        if pause:
            player1.deplacer((bille1.position.x, 0))
        else:
            player1.deplacer(pygame.mouse.get_pos())

        # Gestion des briques
        for t in briques:
            if t.val <= 0:
                briques.remove(t)
            if t.position.x-4 < bille1.position.x < t.position.x + entraxeB+4 and t.position.y-4 < bille1.position.y < t.position.y + entraxeB+4:
                t.val = t.val - 15
                if t.position.x-4 < bille1.position.x < t.position.x+2 or t.position.x + entraxeB-2 < bille1.position.x < t.position.x + entraxeB + 4:
                    bille1.direction.x = -bille1.direction.x

                if t.position.y-4 < bille1.position.y < t.position.y+2 or t.position.y + entraxeB-2 < bille1.position.y < t.position.y + entraxeB + 4:
                    bille1.direction.y = -bille1.direction.y

        # Rebond droite/gauche
        if not bille1.taille <= bille1.position.x <= fen_x - bille1.taille:
            bille1.direction.x = -bille1.direction.x

        # Rebond plafond
        if (bille1.position.y - bille1.taille) <= 0:
            bille1.direction.y = -bille1.direction.y

        # Rebond table
        if (fen_y - (player1.taille / 2) - player1.hauteurplayer) <= (bille1.position.y + bille1.taille) <= (fen_y + (player1.taille / 2) - player1.hauteurplayer) and player1.position.x - player1.largeur <= bille1.position.x <= player1.position.x + player1.largeur:
            if player1.position.x - player1.largeur <= bille1.position.x <= player1.position.x - player1.largeur+20 or player1.position.x + player1.largeur - 20 <= bille1.position.x <= player1.position.x + player1.largeur:
                posx = bille1.direction.x
                bille1.direction.x = -bille1.direction.y
                bille1.direction.y = posx
            else:
                bille1.direction.y = -bille1.direction.y

        #RAZ
        if bille1.position.y >= fen_y - player1.hauteurplayer+20:
           demarrage = False

    else:
        #print(core.getkeyPressValue())

        bille1.deplacer((fen_x / 2, fen_y - player1.hauteurplayer - (player1.taille / 2) - bille1.taille))
        player1.deplacer((fen_x / 2, 0))
        player1.afficher(core)
        bille1.afficher(core)

        if core.getMouseLeftClick():
            bille1.direction.x = 2
            bille1.direction.y = -3
            demarrage = True


if __name__ == '__main__':
    core.main(setup, run)
