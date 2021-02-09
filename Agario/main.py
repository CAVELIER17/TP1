from Agario.player import Player
from p5 import core

if __name__== '__main__':
    mon_joueur = Player()

    def setup():
        print("Setup START---------")
        core.fps = 30
        core.WINDOW_SIZE = [400, 400]


        print("Setup END-----------")


    def run():
       pass


    core.main(setup, run)
