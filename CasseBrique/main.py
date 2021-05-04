import time

import pygame
from pygame.constants import K_p, K_BREAK, K_q

from CasseBrique.Page.accueil import Accueil
from CasseBrique.Page.perdu import Perdu
from CasseBrique.Page.gagne import Gagne
from CasseBrique.Page.pause import Pause
from p5 import core
from CasseBrique.player import Player
from CasseBrique.brique import Brique
from CasseBrique.bille import Bille


# Initialisation Variable
Niveaux = ["Facile", "Intermediaire", "Difficile", "Expert"]
LongueurTXT = [4*35,9*35,6*35,5*35]
Paccueil = []
briques = []
player1 = None
bille1 = None
fen_x = 770
fen_y = 800
dimBTN = (500,90)
entraxeB = 35
demarrage = False
fin = False
pause = False
fronMTPause = None
Score =  0
Zone = 2
tempscore = 0
difficulter = ""

def setup():

    # Initialisation fenetre
    core.fps = 120*2
    core.WINDOW_SIZE = [fen_x, fen_y]
    core.TITLE_WINDOW = "Casse Brique"



    # Initialisation Variable
    global player1, Findelapartie, bille1, Gagner,fontW, pauseT, LongueurTXT
    Findelapartie = Perdu()
    Gagner = Gagne()
    pauseT = Pause()
    fontW = pygame.font.Font('Police/WEST.TTF', 30)

    # Création player, bille, briques
    player1 = Player((fen_x, fen_y))
    bille1 = Bille()
    for i in range(0, 22):
        for j in range(0, 8):
            briques.append(Brique(i * entraxeB, j * entraxeB))

    nb = 0
    for NV in Niveaux:
        posNv = ((fen_x - dimBTN[0]) / 2, 120 + dimBTN[1] * 2 * nb)
        Paccueil.append(Accueil(posNv, dimBTN, NV, (255, 255, 255),LongueurTXT[nb]))
        nb += 1


def run():
    global demarrage, fin, pause, fronMTPause, Score, Findelapartie, tempscore, Gagner, pause

    for b in briques:
        b.afficher(core)

    # Affichage Score

    ScoreT = fontW.render("Score : " + str(Score), True, (255, 255, 255))
    core.screen.blit(ScoreT, (35, fen_y-30))



    if fin:
        if len(briques) != 0:
            Findelapartie.afficher((fen_x, fen_y))
        else:
            Gagner.afficher((fen_x, fen_y))

        if core.getMouseLeftClick():
            fin = False
            demarrage = False
    else:
        if demarrage:

            player1.afficher(core)
            bille1.afficher(core)

            bille1.deplacer((bille1.position.x - bille1.direction.x, bille1.position.y + bille1.direction.y))

            if Score % 5 == 0 and Score != tempscore:
                tempscore = Score
                bille1.direction.x = bille1.direction.x*1.014
                bille1.direction.y = bille1.direction.y*1.014


            # Mode Pause
            if pygame.key.get_pressed()[K_p] and not fronMTPause or not pygame.key.get_pressed()[K_p] and fronMTPause:
                if pygame.key.get_pressed()[K_p] and not fronMTPause:
                    pause = not pause
                fronMTPause = not fronMTPause

            if pause:
                player1.deplacer((bille1.position.x, 0))
                pauseT.afficher((fen_x, fen_y))
            else:
                player1.deplacer(pygame.mouse.get_pos())

            # Gestion des briques
            for t in briques:
                if t.val <= 0:
                    briques.remove(t)
                if t.position.x - Zone < bille1.position.x < t.position.x + entraxeB + Zone and t.position.y - Zone < bille1.position.y < t.position.y + entraxeB + Zone:
                    t.val = t.val - 1
                    Score = Score + 1
                    if t.position.x - Zone < bille1.position.x < t.position.x + Zone/2 or t.position.x + entraxeB - Zone/2 < bille1.position.x < t.position.x + entraxeB + Zone:
                        bille1.direction.x = -bille1.direction.x

                    if t.position.y - Zone < bille1.position.y < t.position.y + Zone/2 or t.position.y + entraxeB - Zone/2 < bille1.position.y < t.position.y + entraxeB + Zone:
                        bille1.direction.y = -bille1.direction.y

            # Rebond droite/gauche
            if not bille1.taille <= bille1.position.x <= fen_x - bille1.taille:
                bille1.direction.x = -bille1.direction.x

            # Rebond plafond
            if (bille1.position.y - bille1.taille) <= 0:
                bille1.direction.y = -bille1.direction.y

            # Rebond table
            if (fen_y - (player1.taille / 2) - player1.hauteurplayer) <= (bille1.position.y + bille1.taille) <= (fen_y + (
                    player1.taille / 2) - player1.hauteurplayer) and player1.position.x - player1.largeur <= bille1.position.x <= player1.position.x + player1.largeur:
                if player1.position.x - player1.largeur <= bille1.position.x <= player1.position.x - player1.largeur + 20 or player1.position.x + player1.largeur - 20 <= bille1.position.x <= player1.position.x + player1.largeur:
                    posx = bille1.direction.x
                    bille1.direction.x = -bille1.direction.y
                    bille1.direction.y = posx
                else:
                    bille1.direction.y = -bille1.direction.y

            # Bille perdu
            if bille1.position.y >= fen_y - player1.hauteurplayer + 20:
                fin = True

            if len(briques) == 0:
                fin = True


        else:

            bille1.deplacer((fen_x / 2, fen_y - player1.hauteurplayer - (player1.taille / 2) - bille1.taille))
            player1.deplacer((fen_x / 2, 0))
            player1.afficher(core)
            bille1.afficher(core)

            for BTN in Paccueil:
                BTN.afficher(core)

            if core.getMouseLeftClick():
                posclic = core.getMouseLeftClick()
                for nv in Paccueil:
                    if nv.BTNclic(posclic):
                        difficulter = nv.texte
                        print(difficulter)
                if difficulter == Niveaux[0]:
                    print(1)
                elif difficulter == Niveaux[1]:
                    print(2)
                elif difficulter == Niveaux[2]:
                    print(3)
                elif difficulter == Niveaux[3]:
                    print(4)
                bille1.direction.x = 1/2
                bille1.direction.y = -1.5/2
                Score = 0
                demarrage = True


if __name__ == '__main__':
    core.main(setup, run)
