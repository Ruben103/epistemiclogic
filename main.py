import os
import numpy as np
import random as rd
from flask_restful import Resource

import Game
import Round
import Player


class playGame(Resource):

    def __init__(self, num_players, believe_parameters, lying_parameters):
        self.game = Game.Game(num_players, believe_parameters, lying_parameters)
        self.game.current_round.controller()


if __name__ == '__main__':
    playGame(4, believe_parameters=[1, 1, 1, 1],
             lying_parameters=[1, 1, 1, 1])  # parameters of each player can be customized

    print("BUGSTOPPER")
