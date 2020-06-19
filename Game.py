import random as rd
import Round as R
import Player as P
from copy import deepcopy
import sys


class Game():

    def __init__(self, num_players, believe_parameters=[], lying_parameters=[]):
        self.players = num_players
        self.players = []
        self.believe_parameters = believe_parameters
        self.lying_parameters = lying_parameters
        self.initialize_players(num_players)
        self.introduce_players()

        # keep track of rounds for information retrieval in later stages
        self.rounds = []
        self.current_round = R.Round(self.players, rd.randint(1, num_players))

        self.add_rounds()
        self.set_KB_of_players()
        self.set_parameters_players()

        self.current_round.controller(rd.choice(self.players))

    def introduce_players(self):
        print("########## Meet the participants #################")
        for player in self.players:
            print("I'm " + str(player.name) + ", and my parameters are:")
            print("Believe parameter: " + str(player.believe_parameter))
            print("Lying parameter: " + str(player.lying_parameter) + "\n")
        print("##################################### START GAME #########################################\n")

    def set_parameters_players(self):
        for p in self.players:
            p.lying_parameter = rd.random()
            p.believe_paramter = rd.random()

    def set_KB_of_players(self):
        for p in self.players:
            p.construct_KB()

    def add_rounds(self):
        self.add_round_to_players(self.current_round)
        self.add_game_to_players(self)
        self.add_game_to_round(self)

    def add_round_to_players(self, round):
        for p in self.players:
            p.add_round(round)

    def add_game_to_round(self, game):
        self.current_round.get_game(game)

    def add_game_to_players(self, game):
        for player in self.players:
            player.add_game(game)

    def remove_player(self, player):
        for p in self.players:
            if p.name == player.name:
                self.players.remove(p)
                print()
        if len(self.players) == 1:
            print("WE HAVE A WINNER!!!\nIts ya boy ", self.players[0].name)
            sys.exit()

    def initialize_players(self, num_players):
        """
        if not self.believe_parameters or not self.lying_parameters:
            for i in range(num_players):
                self.players.append(P.Player(i, game=self))
        else:
        """
        for i in range(num_players):
            self.players.append(P.Player(i, game=self, believe_parameter=self.believe_parameters[i],
                                         lying_parameter=self.lying_parameters[i]))

    def save_round(self, state_of_round):
        self.rounds.append(state_of_round)

    def new_round(self, round, starting_player):
        self.save_round(deepcopy(round))
        self.current_round = R.Round(self.players, starting_player)
        self.set_KB_of_players()
        self.add_rounds()
        print("\n\nROUND NUMBER", len(self.rounds) + 1, "LETS GO")
        self.current_round.controller(self.current_round.starting_player)
