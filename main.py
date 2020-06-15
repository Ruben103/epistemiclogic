import os
import numpy as np
import random as rd
from flask_restful import Resource


class Game():

    def __init__(self, num_players):
        self.players = num_players
        self.players = []
        self.initialize_players(num_players)

        # keep track of rounds for information retrieval in later stages
        self.rounds = []
        self.current_round = Round(self.players, rd.randint(1,num_players))

        self.add_rounds()
        self.set_KB_of_players()

        self.current_round.controller(rd.randint(1,num_players))

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

    def remove_player(self, player):
        for p in self.players:
            if p.name == player.name:
                self.players.remove(p)
        if len(self.players) == 1:
            print("WE HAVE A WINNER!!!\nIts ya boy ", self.players[0].name)
            quit()

    def add_game_to_round(self, game):
        self.current_round.get_game(game)

    def add_game_to_players(self, game):
        for player in self.players:
            player.add_game(game)

    def initialize_players(self, num_players):
        for i in range(num_players):
            self.players.append(Player(i, game=self))

    def save_round(self, state_of_round):
        self.rounds.append(state_of_round)

    def new_round(self, round, starting_player):
        self.save_round(round)
        self.current_round = Round(self.players, starting_player)
        self.add_rounds()
        print("\nROUND NUMBER", len(self.rounds) + 1, "LETS GO\n")
        self.current_round.controller(self.current_round.starting_player)


class Round():

    def __init__(self, players, starting_player):
        # self.game = game
        self.CK = []
        self.players = players
        self.starting_player = starting_player
        self.num_dice = self.count_dice(self.players)

        self.previous_it = None
        self.previous_player = None
        self.curr_bid_num = None
        self.curr_bid_val = None

        self.end_of_bid_phase = False

    def get_num_players(self):
        return len(self.players)

    def get_game(self, game):
        self.game = game

    def update_CK(self, bid_num, bid_val):
        """
        This function updates the Common Knowledge base based on the bids of each player per round.
        Determine probabilistically what the other agents believe the amount
        of dice should be in the hands of the player making a bid and add that to the knowledge base.
        This function should also prompt all of the players' knowledge bases
        :return:
        """
        self.CK.append((bid_num, bid_val))

    def get_total_dice(self):
        tot = 0
        for p in self.players:
            tot += p.get_num_dice()
        return tot

    def next_player(self, it):
        return it + 1 if it + 1 < len(self.players) else 1

    def controller(self, it):
        """
        Haven't tested yet if the iterator gives segmentation errors yet, but the structure should be smt like this
        We iterate over players, players return bid. If they don't believe its possible, they set end_of_bid_phase
        :param it:
        :return:
        """

        player = self.players[it - 1]
        self.previous_it = it
        it = self.next_player(it)
        if not self.end_of_bid_phase:

            bid_num, bid_val = player.ask_bid(self.curr_bid_num, self.curr_bid_val)
            if bid_num == -1 and bid_val == -1:
                self.end_of_bid_phase = True
                self.previous_player.valuation = True
            else:
                self.update_CK(bid_num, bid_val)
                self.curr_bid_num = bid_num; self.curr_bid_val = bid_val
            self.update_player_bids()
            self.previous_player = player
            self.controller(it)
        else:
            print("Valuation was not believed by player. bid_num:", self.curr_bid_num, "bid_val:", self.curr_bid_val)
            for p in self.players:
                if p.valuation is not None:
                    p.is_possible(self.curr_bid_num, self.curr_bid_val)
                p.update_valuation(p.is_possible(self.curr_bid_num, self.curr_bid_val))
                p.print_believes(self.curr_bid_num, self.curr_bid_val)
            self.end_of_round()

    def update_player_bids(self):
        for p in self.players:
            p.curr_bid_val = self.curr_bid_val
            p.curr_bid_num = self.curr_bid_num

    def is_possible(self, dice):
        return dice.count(self.curr_bid_val) < self.curr_bid_num

    def end_of_round(self):
        dice = []
        for p in self.players:
            for d in p.dice:
                dice.append(d)
        valuation = self.is_possible(dice)
        for p in self.players:
            p.remove_dice(valuation)
        self.game.new_round(self, self.previous_it)

        print("BUGSTOPPER")

    def reset_CK(self):
        self.CK = []

    def count_dice(self, players):
        count = 0

        for player in players:
            count += player.get_num_dice()
        return count

class Player():

    def __init__(self, name, game):
        self.name = name
        self.num_dice = 6
        self.dice = self.init_dice(self.num_dice)
        self.KB = []

        self.curr_bid_num = None
        self.curr_bid_val = None
        self.valuation = None


    def add_game(self, game):
        self.game = game

    def construct_KB(self):

        # for each player still in the game,  make an array based on the size of the dice stack of those players
        for p in self.game.players:
            if p.name != self.name:
                self.KB.append([])
            else:
                self.KB.append(self.dice)
        self.KB = np.asarray(self.KB)

    def get_dice(self):
        return self.dice

    def add_round(self, round):
        self.round = round

    def update_dice(self, new):
        self.num_dice = new

    def update_KB(self):
        self.KB = self.dice

    def get_num_dice(self):
        return self.num_dice

    def get_amount_dice(self, val):
        # return amount of dice of a certain value
        return self.dice.count(val)

    def amount_possible(self, tot, num, val):
        return int(tot / 3)

    def update_valuation(self, valuation):
        self.valuation = valuation

    def init_dice(self, num_dice):
        dice = []
        for i in range(num_dice):
            dice.append(rd.randint(1, 6))
        return sorted(dice)

    def remove_dice(self, valuation):

        if self.valuation != valuation:
            print("Player", self.name, "'s valuation is incorrect \nOne dice is removed from his stock")
            if self.num_dice > 1:
                self.num_dice -= 1
            else:
                self.num_dice -= 1
                self.round.game.remove_player(self)
                print("\n",self.name, "'s dice stock is completely empty. He is out of the game")
        else:
            print("Player", self.name, "'s valuation is correct \nNO dice is removed from his stock")

    def is_possible(self, bid_num, bid_val):
        tot = self.round.get_total_dice()
        amount = self.amount_possible(tot, bid_num, bid_val) + self.get_amount_dice(bid_val)
        return amount >= bid_num

    def print_believes(self, num, val):
        if self.is_possible(num, val):
            print("\nI'm", self.name, "and I believe this bid because:", "\nI have", self.get_amount_dice(val), val, "'s", "\nThe rest probably has:", self.amount_possible(self.round.get_total_dice(), num, val))
        else:
            print("\nI'm", self.name, "and I do NOT believe this because:", "\nI have", self.get_amount_dice(val), val, "'s", "\nThe rest probably has:", self.amount_possible(self.round.get_total_dice(), num, val))

    def decision_table(self):
        table = np.ndarray((2,6))
        table = table.astype(int)
        table[0,:] = [1, 2, 3, 4, 5, 6]

        for col in range(table.shape[1]):
            value = table[0][col]
            cnt = 0
            for p_it in range(len(self.KB)):
                # should account for the count of the player's own dice
                if value not in self.KB[p_it]:
                    # account for the probability of having them if the value is not in KB of that player
                    cnt += int((self.round.players[p_it].get_num_dice() - len(self.KB[p_it])) / 3)
                else:
                    curr_count = self.KB[p_it].count(value)
                    cnt += curr_count
            table[1][value - 1] = cnt
        return table

    def pick_from_decision_table(self, table):
        table = table.transpose()
        max_table = table[table[:, 1] == np.max(table[:, 1])].transpose()
        if len(max_table[0]) == 1:
            print("")
        pick = np.random.randint(len(max_table[0]))
        num = max_table[1][pick]; val = max_table[0][pick]

        return int(num), int(val)

    def ask_bid(self, bid_num, bid_val):
        """
        This function makes a bid based on the players KB.
        The player needs to make a higher offer than the previous one. (Round.curr_bid_num, Round.curr_bid_val).
        :return: tuple: bid_num, bid_val
        """
        if bid_num is not None and bid_val is not None:
            if self.is_possible(bid_num, bid_val):
                decision_table = self.decision_table()
                num, val = self.pick_from_decision_table(decision_table)
                while self.curr_bid_num is not None and num <= self.curr_bid_num:
                    num += 1
                return num, val
            else:
                print("First player not to believe:")
                self.print_believes(bid_num, bid_val)
                self.valuation = False
                return -1, -1
        else:
            return 1, 2


class playGame(Resource):
    game = Game(num_players=4)
    game.current_round.controller(game.current_round.starting_player)

    print("BUGSTOPPER")


if __name__ == '__main__':
    game = Game(num_players=4)
    game.current_round.controller(game.current_round.starting_player)

    print("BUGSTOPPER")