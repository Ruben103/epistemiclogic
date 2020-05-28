import os
import numpy as np
import random as rd

class Game():

    def __init__(self, num_players):
        self.players = num_players
        self.players = []
        self.initialize_players(num_players)

        # keep track of rounds for information retrieval in later stages
        self.rounds = []
        self.current_round = Round(self.players, rd.randint(1,num_players), game=self)

    def initialize_players(self, num_players):
        for i in range(1, num_players + 1):
            self.players.append(Player(name='P' + str(i), game=self), round=self.current_round)

    def save_round(self, state_of_round):
        self.rounds.append(state_of_round)


class Round():

    def __init__(self, players, starting_player, game):
        self.game = game
        self.CK = []
        self.players = players
        self.starting_player = starting_player
        self.num_dice = self.count_dice()

        self.curr_bid_num = None
        self.curr_bid_val = None

        self.end_of_bid_phase = False

    def update_CK(self, bid_num, bid_value):
        """
        This function updates the Common Knowledge base based on the bids of each player per round.
        Determine probabilistically what the other agents believe the amount
        of dice should be in the hands of the player making a bid and add that to the knowledge base.
        This function should also prompt all of the players' knowledge bases
        :return:
        """
        pass

    def controller(self, it):
        """
        Haven't tested yet if the iterator gives segmentation errors yet, but the structure should be smt like this
        We iterate over players, players return bid. If they don't believe its possible, they set end_of_bid_phase
        :param it:
        :return:
        """

        current_player = self.players(it - 1)
        if not self.end_of_bid_phase:

            bid_num, bid_val = current_player.ask_bid()
            self.update_CK(bid_num, bid_val)
            self.controller(it = it + 1 if it + 1 != len(self.players) else 0)
        else:
            for p in self.players:
                if p.valuation is not None:
                    current_player.val_bid(self.curr_bid_num, self.curr_bid_val)
            self.end_of_round()

    def is_possible(self, dice):
        pass

    def end_of_round(self):
        dice = []
        for p in self.players:
            dice.append(p.dice)
        valuation = self.is_possible(dice)
        for i in range(len(self.players)):
            p = self.players(i)
            p_eval = p.remove_dice(valuation)
            if p_eval == True:
                print("Player", i, "'s valuation is correct \n no dice is removed from his stock")
            if p_eval == False:
                print("Player", i, "'s valuation is false \n one dice is removed from his stock")
        self.save_round(self)
        self.reset_CK()
        self.controller(self.starting_player)

    def reset_CK(self):
        self.CK = []

    def count_dice(self, players):
        count = 0
        for player in players:
            count += player.get_num_dice()
        return count


class Player():

    def __init__(self, name, round):
        self.name = name
        self.num_dice = 6
        self.dice = self.init_dice(self.num_dice)
        self.KB = []
        self.update_KB()

        self.curr_bid_num = None
        self.curr_bid_val = None
        self.valuation = None

    def init_dice(self, num_dice):
        dice = []
        for i in range(num_dice):
            dice.append(rd.randint(1, 6))
        return sorted(dice)

    def update_dice(self, new):
        self.num_dice = new

    def update_KB(self):
        self.KB = self.dice

    def get_num_dice(self):
        return self.num_dice

    def is_possible(self, bid_num, bid_val):
        pass

    def ask_bid(self):
        """
        This function makes a bid based on the players KB.
        The player needs to make a higher offer than the previous one. (Round.curr_bid_num, Round.curr_bid_val).
        :return: tuple: bid_num, bid_val
        """
        if self.is_possible(self.curr_bid_num, self.curr_bid_val):
            # give a higher bid.
            pass
            # return bid_num, bid_val
        else:
            pass
            # return False, False

    def val_bid(self, bid_num, bid_val):
        """
        This function is prompted when the bidding phase is over.
        :param bid_num:
        :param bid_val:
        :return: return T/F for whether they believe the current bid is possible or not.
        """
        pass

if __name__ == '__main__':
    game = Game(num_players=4)

    print("BUGSTOPPER")