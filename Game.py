import random as rd
import Round as R
import Player as P
from copy import deepcopy

class Game():

    def __init__(self, num_players):
        self.players = num_players
        self.players = []
        self.initialize_players(num_players)

        # keep track of rounds for information retrieval in later stages
        self.rounds = []
        self.current_round = R.Round(self.players, rd.randint(1,num_players))

        self.add_rounds()
        self.set_KB_of_players()

        self.current_round.controller(rd.choice(self.players))

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
        if len(self.players) == 1:
            print("WE HAVE A WINNER!!!\nIts ya boy ", self.players[0].name)
            quit()

    def initialize_players(self, num_players):
        for i in range(num_players):
            self.players.append(P.Player(i, game=self))

    def save_round(self, state_of_round):
        self.rounds.append(state_of_round)

    def new_round(self, round, starting_player):
        self.save_round(deepcopy(round))
        self.current_round = R.Round(self.players, starting_player)
        self.set_KB_of_players()
        self.add_rounds()
        print("\nROUND NUMBER", len(self.rounds) + 1, "LETS GO")
        self.current_round.controller(self.current_round.starting_player)
