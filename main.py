import os
import numpy as np
import random as rd
from flask_restful import Resource

import Game
import Round
import Player


class playGame(Resource):

    def __init__(self, num_players):
        self.game = Game.Game(num_players)

        self.game.current_round.controller()

if __name__ == '__main__':

    playGame(4)


    print("BUGSTOPPER")