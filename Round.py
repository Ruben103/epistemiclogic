import numpy as np
import Game as G
import Player as P

class Round():

    def __init__(self, players, starting_player):
        # self.game = game
        self.CK = []
        self.players = players
        self.starting_player = starting_player
        self.num_dice = self.count_dice(self.players)

        self.previous_it = None
        self.previous_player = None
        self.curr_num = None
        self.curr_val = None

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

            bid_num, bid_val = player.bid(self.curr_num, self.curr_val)
            if bid_num == -1 and bid_val == -1:
                self.end_of_bid_phase = True
                self.previous_player.valuation = True
            else:
                self.update_CK(bid_num, bid_val)
                self.curr_num = bid_num; self.curr_val = bid_val
            self.update_player_bids()
            self.previous_player = player
            self.controller(it)
        else:
            print("Valuation was not believed by player. bid_num:", self.curr_num, "bid_val:", self.curr_val)
            for p in self.players:
                if p.valuation is not None:
                    p.is_possible(self.curr_num, self.curr_val)
                p.update_valuation(p.is_possible(self.curr_num, self.curr_val))
                p.print_believes(self.curr_num, self.curr_val)
            self.end_of_round()

    def update_player_bids(self):
        for p in self.players:
            p.curr_bid_val = self.curr_val
            p.curr_bid_num = self.curr_num

    def is_possible(self, dice):
        return dice.count(self.curr_val) <= self.curr_num

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

    def count_dice(self, players):
        count = 0

        for player in players:
            count += player.get_num_dice()
        return count