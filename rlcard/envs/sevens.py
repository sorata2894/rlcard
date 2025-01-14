import sys
import os
sys.path.append(os.path.abspath("D:\\rlcard\\rlcard"))

import numpy as np
from collections import OrderedDict
from rlcard.envs import Env

# from games.Sevens.game import SevensGame as Game
from games.sevens import Game
from games.sevens.util import encode_hand, encode_target
from games.sevens.util import ACTION_SPACE, ACTION_LIST
from games.sevens.util import card2list

DEFAULT_GAME_CONFIG = { 'game_num_players' : 4 }

class SevensEnv(Env):
    
    def __init__(self, config):
        self.name = 'sevens'
        self.default_game_config = DEFAULT_GAME_CONFIG
        self.game = Game()
        super().__init__(config)
        self.state_shape = []
        self.action_shape = [None for _ in range(self.num_players)]
    
    def _extract_state(self, state):
        obs = np.zeros((), dtype=int)
        encode_hand(obs[:3], state['hand'])
        encode_target(obs[:3], state['target'])
        legal_action_id = self._get_legal_actions()
        extracted_state = {'obs': obs, 'legal_actions': legal_action_id}
        extracted_state['raw_obs'] = state
        extracted_state['raw_legal_actions'] = [a for a in state['legal_actions']]
        extracted_state['action_record'] = self.action_recorder
        return extracted_state

    def get_payoffs(self):

        return np.array(self.game.get_payoffs())

    def _decode_action(self, action_id):
        legal_ids = self._get_legal_actions()
        if action_id in legal_ids:
            return ACTION_LIST[action_id]
        
        return ACTION_LIST[np.random.choice(legal_ids)]

    def _get_legal_actions(self):
        legal_actions = self.game.get_legal_actions()
        legal_ids = {ACTION_SPACE[action]: None for action in legal_actions}
        return OrderedDict(legal_ids)

    def get_perfect_information(self):
        state = {}
        state['num_players'] = self.num_players
        state['hand_cards'] = [cards2list(player.hand)
                               for player in self.game.players]
        state['played_cards'] = cards2list(self.game.round.played_cards)
        state['target'] = self.game.round.target.str
        state['current_player'] = self.game.round.current_player
        state['legal_actions'] = self.game.round.get_legal_actions(
            self.game.players, state['current_player'])
        return 