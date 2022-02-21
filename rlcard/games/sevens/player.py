from itertools import count
from numpy.lib.function_base import select

from games.sevens.util import VAL_MAP

class SevensPlayer:

    def __init__(self, player_id, np_random):

        '''
            Initilize a player

            Args:
                player_id (int): The id of the player
        '''
        self.np_random = np_random
        self.player_id = player_id
        self.hand = []
        self.cover = []
        self.stack = []
        self.coverpoint = 0

    def get_player_id(self):

        '''
            Return the id of the player
        '''

        return self.player_id
    
    def print_hand(self):
        
        '''
            Print the cards in hand in string
        '''
        print([c.get_str() for c in self.hand])

    def play_card(self, dealer, card):
        
        '''
            Play one card

            Args:
                dealer (object) : Dealer
                Card (object): The card to be play
        '''
        if card.val[0] != 'a':
            card = self.hand.pop(self.hand.index(card))
            if card.flower == 'C':
                dealer.tabel[0].append(card)
            elif card.flower == 'D':
                dealer.tabel[1].append(card)
            elif card.flower == 'H':
                dealer.tabel[2].append(card)
            elif card.flower == 'S':
                dealer.tabel[3].append(card)
                
        elif card.val[0] == 'a':
            card.val.pop(0)
            card = self.hand.pop(self.hand.index(card))
            self.cover.append(card)
            self.count_coverpoint()
    
    def count_coverpoint(self):

        '''
            Count player cover point
        '''
        point = 0
        for a in self.cover:
            point += VAL_MAP(a.val)

        self.coverpoint = point

