from player import SevensPlayer
from card import SevensCard
from games.sevens.util import card2list
VAL_MAP = {'A':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12,'aA':14, 'a2':13, 'a3':14, 'a4':15, 'a5':16, 'a6':18, 'a7':19, 'a8':20, 'a9':21, 'aT':22, 'aJ':23, 'aQ':24, 'aK':25}

class SevensRound:

    def __init__(self, dealer, judger ,num_players, np_random):
        '''
            Initialize the round class

            Args:
                dealer(object): the object of SevensDealer
                num_players (int): the number of players in game
        '''
        self.np_random = np_random
        self.judger = judger
        self.dealer = dealer
        self.target = None
        self.current_player = 0
        self.num_players = num_players
        self.direction = 1
        self.played_cards = []
        self.is_over = False
        self.winner = None
    
    def proceed_round(self, players, action):
        '''
            Call other Classes's functions to keep one round running

            Args:
                player (object): object of SevensPlayer
                action (str): string of legal action
        '''
        player = players[self.current_player]
        card_info = action.split('-')
        val = card_info[0]
        flower = card_info[1]
        player.play_card(self.dealer, action)
        self.last_player = self.current_player
        self.current_player = (self.current_player + 1) % 4
    
    # TODO 要把legal_actions 寫完
    # reference https://github.com/datamllab/rlcard/blob/c21ea82519c453a42e3bdc6848bd3356e9b6ac43/rlcard/games/uno/round.py
    def get_legal_actions(self, players, player_id):
        legal_action = []
        hand = players[player_id].hand
        target = self.target
        have_card = 0
        for card in hand:
            for a in target:
                if card.flower == a.flower:
                    if int(VAL_MAP(card.val)) == int(VAL_MAP(a.val)):
                        legal_action.append(card)
                        have_card = 1
        if have_card == 0:
            for card in hand:
                card.val = 'a'+card.val
                legal_action.append(card)
        
        return legal_action
                
        
    

    def get_state(self, players, player_id):
        '''
            Get player's state

            Args:
                players (list): The list of SevensPlayer
                player_id (int): The id of the player
        '''

        state = {}
        player = players[player_id]
        state['hand'] = card2list(player.hand)
        state['target'] = self.target.str
        state['played_cards'] = card2list(self.played_cards)
        state['legal_actions'] = self.get_legal_actions(players, player_id)
        state['num_cards'] = []
        for player in players:
            state['num_cards'].append(len(player.hand))
        return state




