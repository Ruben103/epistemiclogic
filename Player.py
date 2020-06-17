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

    def add_game(self, game):
        self.game = game

    def construct_KB(self):

        # for each player still in the game,  make an array based on the size of the dice stack of those players
        self.KB = []
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
        prob = 6 if val == 1 else 3
        return int(tot / prob)

    def update_valuation(self, valuation):
        self.valuation = valuation

    def roll_dice(self):
        self.dice = []
        for i in range(self.num_dice):
            self.dice.append(rd.randint(1, 6))
        self.dice = sorted(self.dice)

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
        if bid_val == 1:
            print("")
        amount = self.amount_possible(tot, bid_num, bid_val) + self.get_amount_dice(bid_val)
        return amount >= bid_num

    def print_believes(self, num, val):
        if self.is_possible(num, val):
            print("\nI'm", self.name, "and I believe this bid because:", "\nI have", self.get_amount_dice(val), val, "'s", "\nThe rest probably has:", self.amount_possible(self.round.get_total_dice(), num, val))
        else:
            print("\nI'm", self.name, "and I do NOT believe this because:", "\nI have", self.get_amount_dice(val), val, "'s", "\nThe rest probably has:", self.amount_possible(self.round.get_total_dice(), num, val))

    def count_unknown_dice(self):
        count = 0
        for KB in self.KB:
            index = np.where(self.KB == KB)[0]

        return count

    def update_KB_of(self, player_it, num, val):
        num_dice_player = self.round.current_player.get_num_dice()
        total_dice = self.round.get_total_dice()
        rest = total_dice - num_dice_player

        # unknown_dice = self.count_unknown_dice()

        believe = rd.random()

        have = int(rest/3) - num
        new_KB = []
        if believe < .5:
            if have > 1 and have < num_dice_player:
                for i in range(have):
                    new_KB.append(val)
            else:
                for i in range(num_dice_player):
                    new_KB.append(val)
        else:
            if len(self.KB[player_it]) < num_dice_player:
                self.KB[player_it].append(val)
            else:
                print("I have no clue what this player is doing")
        self.KB[player_it] = new_KB
        print("")



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
        if len(max_table[0]) == 1:
            print("")
        pick = np.random.randint(len(max_table[0]))
        num = max_table[1][pick]; val = max_table[0][pick]

        return int(num / 2) if val == 1 else int(num), int(val)

    def bid(self, bid_num, bid_val):
        """
        This function makes a bid based on the players KB.
        The player needs to make a higher offer than the previous one. (Round.curr_bid_num, Round.curr_bid_val).
        :return: tuple: bid_num, bid_val
        """
        if bid_num is not None and bid_val is not None:
            if self.is_possible(bid_num, bid_val):
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
                return num, val
            else:
                print("First player not to believe:")
                self.print_believes(bid_num, bid_val)
                self.valuation = False
                self.round.previous_player.valuation = True
                return -1, -1
        else:
            return 1, 2