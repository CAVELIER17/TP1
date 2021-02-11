from Agario.bille import Bille
from Agario.creep import Creep
from Agario.player import Player
from p5 import core

player1 = None
creeps = []
bille = Bille()

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    global player1
    player1 = Player()
    for i in range(0, 1000):
        creeps.append(Creep(800,800))
    print("Setup END-----------")

def run():
    print("Run")
    for c in creeps:
        c.afficher(core)


    player1.afficher(core)
    if core.getMouseLeftClick() is not None:
        player1.deplacer(core.getMouseLeftClick())


if __name__== '__main__':
    core.main(setup, run)
