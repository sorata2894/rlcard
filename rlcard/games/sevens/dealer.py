# import sys
# import os
# sys.path.append(os.path.abspath("D:\\rlcard\\rlcard\\games\\sevens"))
# -*- coding: utf-8 -*-
from util import init_deck
from rlcard.utils import init_standard_deck

class SevensDealer:
    
    '''
        Initalize a Sevens dealer class
    '''

    def __init__(self, np_random):
        self.np_random = np_random
        self.deck = init_standard_deck()
        self.shuffle()
        self.table = [[],[],[],[]]
    
    def shuffle(self):

        '''
            Shuffle the deck
        '''
        self.np_random.shuffle(self.deck)
    
    def deal_cards(self, player, num):

        '''
            Deal 13 cards fom deck to one player

            Args:
                player (object): The object of Sevens_game_Player
                num (int): The number of cards to dealed
        '''

        for _ in range(num):
            player.hand.append(self.deck.pop())
