import numpy as np
import random as rd
import Game
import Round

class Player():

    def __init__(self, name, game):
        self.name = name
        self.num_dice = 6
        self.dice = self.roll_dice()
        self.KB = []

        self.curr_bid_num = None
        self.curr_bid_val = None
        self.valuation = None

        self.believe_parameter = 1
        self.lying_parameter = 1

    def add_game(self, game):
        self.game = game

    def reset_num_val(self):
        self.curr_bid_num = self.curr_bid_val = None

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

    def update_valuation(self, valuation):
        self.valuation = valuation

    def roll_dice(self):
        self.dice = []
        for i in range(self.num_dice):
            self.dice.append(rd.randint(1, 6))
        self.dice = sorted(self.dice)

    def construct_KB(self):
        # for each player still in the game,  make an array based on the size of the dice stack of those players
        self.KB = []
        for p in self.round.players:
            if p.name != self.name:
                self.KB.append([])
            else:
                self.KB.append(self.dice)
        self.KB = np.asarray(self.KB)

    def remove_dice(self, valuation):

        if self.valuation != valuation:
            print("\nPlayer", self.name, "'s valuation is incorrect, One dice is removed from his stock")
            if self.num_dice > 1:
                self.num_dice -= 1
            else:
                print("\n", self.name, "'s dice stock is completely empty. He is out of the game")
                self.num_dice -= 1
                self.round.game.remove_player(self)
        else:
            print("\nPlayer", self.name, "'s valuation is correct, NO dice is removed from his stock")

    def amount_possible(self, tot, val):
        prob = 6 if val == 1 else 3
        return int(tot / prob)

    def is_possible(self, num, val):
        if num == 1 and val == 2:
            # make sure to always make a bid in the beginning
            return True
        count = 0
        # count the number of dice in belief structure
        for KB in self.KB:
            count += KB.count(val)
        tot = self.round.get_total_dice()
        amount_left = tot - count
        amount = count + self.amount_possible(amount_left, val)
        return amount >= num

    def print_believes(self, num, val):
        if self.is_possible(num, val):
            print("I'm Player", self.name, "I believe this bid. Valuation:", self.valuation)
        else:
            print("I'm Player", self.name, "I DO NOT believe this bid.", self.valuation)

    def fill_KB(self, avail, it, val):
        for i in range(avail):
            self.KB[it].append(val)

    def update_KB_of(self, player_it, num, val):
        num_dice_player = self.round.current_player.get_num_dice()
        total_dice = self.round.get_total_dice()
        rest = total_dice - num_dice_player

        believe = rd.random()

        if believe < self.believe_parameter:
            # Then the player should believe this bid.
            prob = 6 if val == 1 else 3
            dice_available = num_dice_player - len(self.KB[player_it])
            num_dice = int(rest / prob) - num
            if num_dice > dice_available:
                num_dice = dice_available
            self.fill_KB(dice_available, player_it, val)
        else:
            if believe < self.believe_parameter/2:
                # Then the player believes so strongly that the player is lying, that he revises his beliefs.
                # If this happens, it also corresponds to the player being confused and forgetting the previous bids.
                self.KB[player_it] = []

    def decision_table(self):
        table = np.ndarray((2,6))
        table = table.astype(int)
        table[0,:] = [1, 2, 3, 4, 5, 6]

        for col in range(table.shape[1]):
            value = table[0][col]
            cnt = 0
            for p_it in range(len(self.KB)):
                # should account for the count of the player's own dice
                prob = 6 if value == 1 else 3
                if value not in self.KB[p_it]:
                    # account for the probability of having them if the value is not in KB of that player
                    cnt += int((self.round.players[p_it].get_num_dice() - len(self.KB[p_it])) / prob)
                else:
                    curr_count = self.KB[p_it].count(value)
                    cnt += curr_count
            table[1][value - 1] = cnt
        table[1,0] = table[1][0] * 2
        return table

    def pick_from_decision_table(self, table):
        table = table.transpose()
        max_table = table[table[:, 1] == np.max(table[:, 1])].transpose()
        pick = np.random.randint(len(max_table[0]))
        num = max_table[1][pick]; val = max_table[0][pick]

        return int(num / 2) if val == 1 else int(num), int(val)

    def bid(self, num, val):
        """
        This function makes a bid based on the players KB.
        The player needs to make a higher offer than the previous one. (Round.curr_bid_num, Round.curr_bid_val).
        :return: tuple: bid_num, bid_val
        """
        if num is not None and val is not None:
            if self.is_possible(num, val):
                decision_table = self.decision_table()
                num, val = self.pick_from_decision_table(decision_table)

                if self.curr_bid_val != 1:
                    # previous bid is not 1
                    if val == 1:
                        while self.curr_bid_num is not None and num * 2 <= self.curr_bid_num:
                            num += 1
                    else:
                        while self.curr_bid_num is not None and num <= self.curr_bid_num:
                            num += 1
                else:
                    # previous bid was 1
                    if val == 1:
                        while self.curr_bid_num is not None and num <= self.curr_bid_num:
                            num += 1
                    else:
                        # current bid is not 1
                        while self.curr_bid_num is not None and num*2 + 1 < self.curr_bid_num:
                            num += 1
                lying = rd.random()
                if lying < self.lying_parameter:
                    if val == 1:
                        num *= 2
                    val = rd.randint(2,6)
                return num, val
            else:
                self.print_believes(num, val)
                self.valuation = False
                return -1, -1
        else:
            return 1, 2