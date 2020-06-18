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
        self.reset_num_val_players()

    def reset_num_val_players(self):
        for p in self.players:
            p.reset_num_val()

    def roll_dice(self):
        for p in self.players:
            p.roll_dice()

    def get_num_players(self):
        return len(self.players)

    def get_game(self, game):
        self.game = game

    def get_all_dice(self):
        dice = []
        for p in self.players:
            for d in p.dice:
                dice.append(d)
        return dice

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
            print("Current player:", self.current_player.name)
            num, val = self.current_player.bid(self.curr_num, self.curr_val)

            if num == -1 and val == -1:
                print("I do not believe the previous bid: ", self.curr_num, self.curr_val)
                self.end_of_bid_phase = True
                self.previous_player.valuation = True
                self.controller(self.current_player)
            else:
                print("I RAISE the previous bid to: : ", num, val)
                self.update_CK(num, val)
                self.curr_num = num; self.curr_val = val
            self.update_KB_of_players(num, val)
            self.update_player_bids()
            self.previous_player = self.current_player
            self.current_player = self.next_player(self.previous_player)
            self.controller(self.current_player)
        else:
            print("======================================\nVALUATION OF PLAYERS\n======================================")
            for p in self.players:

                if p.valuation is None:
                    valuation = p.is_possible(self.curr_num, self.curr_val)
                    p.valuation = valuation
                if p.name == self.previous_player.name:
                    print("I'm player", p.name, "my bid was not believed. Valuation:", p.valuation)
                elif p.name == self.current_player.name:
                    p.print_believes(self.curr_num, self.curr_val)
                    print("Because it was my bid.")
                else:
                    p.print_believes(self.curr_num, self.curr_val)
            self.end_of_round()

    def end_of_round(self):
        dice = self.get_all_dice()
        valuation = self.is_possible(dice)
        print("\nThe actual VALUATION was:", str(valuation), "Therefore:\n")
        for p in self.players:
            p.remove_dice(valuation)
        self.game.new_round(self, self.current_player)

        print("BUGSTOPPER")

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

    def count_dice(self, players):
        count = 0

        for player in players:
            count += player.get_num_dice()
        return count