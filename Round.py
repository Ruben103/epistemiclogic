import numpy as np
import Game as G
import Player as P

class Round():

    def __init__(self, players, starting_player):
        self.CK = []
        self.players = players
        self.starting_player = starting_player
        self.num_dice = self.count_dice(self.players)

        self.previous_it = None
        self.previous_player = None

        self.current_it = None
        self.current_player = None
        self.curr_num = 1
        self.curr_val = 2

        self.end_of_bid_phase = False
        self.roll_dice()

    def roll_dice(self):
        for p in self.players:
            p.roll_dice()

    def get_num_players(self):
        return len(self.players)

    def get_game(self, game):
        self.game = game

    def update_CK(self, bid_num, bid_val):
        self.CK.append((bid_num, bid_val))

    def get_total_dice(self):
        tot = 0
        for p in self.players:
            tot += p.get_num_dice()
        return tot

    def next_player(self, it):
        it = self.players.index(self.current_player)
        return self.players[it + 1 if it + 1 < len(self.players) else 0]

    def controller(self, player):
        """
        Haven't tested yet if the iterator gives segmentation errors yet, but the structure should be smt like this
        We iterate over players, players return bid. If they don't believe its possible, they set end_of_bid_phase
        :param it:
        :return:
        """
        self.current_player = player
        if not self.end_of_bid_phase:

            num, val = player.bid(self.curr_num, self.curr_val)
            if num == -1 and val == -1:
                self.end_of_bid_phase = True
                self.previous_player.valuation = True
            else:
                self.update_CK(num, val)
                self.curr_num = num; self.curr_val = val
            self.update_KB_of_players(num, val)
            self.update_player_bids()
            self.previous_player = self.current_player
            self.current_player = self.next_player(self.previous_player)
            self.controller(self.current_player)
        else:
            print("Valuation was not believed by player. bid_num:", self.curr_num, "bid_val:", self.curr_val)
            for p in self.players:
                if p.valuation is not None:
                    p.is_possible(self.curr_num, self.curr_val)
                p.update_valuation(p.is_possible(self.curr_num, self.curr_val))
                p.print_believes(self.curr_num, self.curr_val)
            self.end_of_round()

    def update_KB_of_players(self, bid, val):
        for p in self.players:
            if p.name != self.current_player.name:
                p.update_KB_of(self.players.index(self.current_player), bid, val)

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
        self.game.new_round(self, self.previous_player)

        print("BUGSTOPPER")

    def count_dice(self, players):
        count = 0

        for player in players:
            count += player.get_num_dice()
        return count