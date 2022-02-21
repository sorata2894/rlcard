#!/usr/bin/env python3
from copy import deepcopy
import numpy as np

from dealer import SevensDealer as Dealer
from player import SevensPlayer as Player
from round  import SevensRound  as Round
from judger import SevensJudger as Judger



class SevensGame:

    def __init__(self, allow_step_back=False, num_players = 4):
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        self.num_players = num_players
        self.payoffs = [0 for _ in range(self.num_players)]

    def configure(self, game_config):
        '''
            Specifiy some secific parameters, such as number of players
        '''
        self.num_players = game_config['game_num_players']

    def init_game(self):
        '''
            Initialiaze players and state

            Returns:
                (tuple): Tuple containing:

                    (dict): The first state in one game
                    (int): Current Player's id
        '''
        # Initialize payoffs
        self.payoffs = [0 for _ in range(self.num_players)]

        # Initaialize a dealer that can deal cards
        self.dealer = Dealer(self.np_random)

        # Initialize four players to play the game
        self.players = [Player(i, self.np_random) for i in range(self.num_players)]

        # Deal 13 cards to each player for all game
        for player in self.players:
            self.dealer.deal_cards(player, 13)

        # Initialize a Round
        self.judger = Judger(self.np_random)
        self.round = Round(self.dealer, self.num_players, self.np_random)

        # Save the history for stepping back to the last state.
        self.history = []

        # Table card
        self.table = []

        player_id = self.round.current_player
        state = self.get_state(player_id)
        return state, player_id

    def step(self, action):
        '''
            Get the next state

            Args:
                action(str): A specific action

            Returns:
                (tuple): Tuple contaning : 

                    (dict): next player's state
                    (int): next plater's id
        '''

        if self.allow_step_back:
            # First snapshot the current state
            his_dealer = deepcopy(self.dealer)
            his_round = deepcopy(self.round)
            his_players = deepcopy(self.players)
            self.history.append((his_dealer, his_players, his_round))

        self.round.proceed_round(self.players, action)
        player_id = self.round.current_player
        state = self.get_state(player_id)
        return state, player_id
    
    def step_back(self):
        '''
            Return to the previous state of the game

            Returns:
                (bool): True if the game steps back successfully
        '''

        if not self.history:
            return False
        self.dealer, self.players, self.round = self.history.pop()
        return True

    def get_state(self, player_id):
        ''' 
            Return player's state

            Args:
                player_id (int): player id

            Returns:
                (dict): The state of the player
        '''
        state = self.round.get_state(self.players, player_id)
        state['num_players'] = self.get_num_players()
        state['current_player'] = self.round.current_player
        return state

    def get_payoffs(self):
        ''' 
            Return the payoffs of the game

            Returns:
                (list): Each entry corresponds to the payoff of one player
        '''
        winner = self.round.winner
        if winner is not None and len(winner) == 1:
            self.payoffs[winner[0]] = 1
            self.payoffs[1 - winner[0]] = -1
        return self.payoffs

    def get_legal_actions(self):
        ''' 
            Return the legal actions for current player

            Returns:
                (list): A list of legal actions
        '''

        return self.round.get_legal_actions(self.players, self.round.current_player)

    def get_num_players(self):
        ''' 
            Return the number of player
            
            Returns:
                (int): The number of players in the game
        '''
        return self.num_players

    @staticmethod
    def get_num_actions():
        ''' 
            Return the number of applicable actions

            Returns:
                (int): The number of actions. There are 52 actions
        '''
        return 104

    def get_player_id(self):
        ''' 
            Return the current player's id
            
            Returns:
                (int): current player's id
        '''
        return self.round.current_player

    def is_over(self):
        ''' 
            Check if the game is over

            Returns:
                (boolean): True if the game is over
        '''
        winner = []
        is_over, winner = self.judger.judge_winner(self.players)
        if is_over:
            return winner
        else:
            return False