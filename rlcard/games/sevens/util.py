import sys
import os
sys.path.append(os.path.abspath("D:\\rlcard\\rlcard\\games\\sevens"))


import json
import numpy as np

import rlcard

from collections import OrderedDict
from card import SevensCard as Card

# Read required docs
ROOT_PATH = rlcard.__path__[0]
ROOT_PATH2 = 'D:\\rlcard\\rlcard'

# a map of abstract action to its index and a list of abstract action
with open(os.path.join(ROOT_PATH2, 'games\\sevens\\jasondata\\action_space.json'), 'r')as file:
    ACTION_SPACE = json.load(file, object_pairs_hook=OrderedDict)
    ACTION_LIST = list(ACTION_SPACE.keys())
# print(ACTION_SPACE)
# print(ACTION_LIST)
FlOWER_MAP = {'C' : 0, 'D': 1, 'H' : 2 , 'S' : 3}

VAL_MAP = {'A':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12}

def init_deck():
    
    '''
        Generate Sevens deck of 52 cards
    '''
    deck = []
    card_info = Card.info
    for flower in card_info['flower']:

        #init number cards
        for val in card_info['val']:
            deck.append(Card('number', val, flower))
    return deck

def card2list(cards):

    cards_list = []
    for card in cards:
        cards_list.append(card.get_str())
    return cards_list

# print(card2list(init_deck()))

def hand2dict(hand):
    
    '''
    
    '''
    hand_dict = {}
    for card in hand:
        if card not in hand_dict:
            hand_dict[card] = 1
        else:
            hand_dict[card] += 1
    return hand_dict



def encode_hand(plane, hand):
    
    '''
        plane is a 3*4*13 numpy array
        
        plane 0 = hand_card
        plane 1 = played_card
        plane 2 = cover_card
        plane 3 = target_card
    '''

    hand = hand2dict(hand)
    for card, count in hand.items():
        card_info = card.split('-')
        val = VAL_MAP[card_info[0]]
        flower = FlOWER_MAP[card_info[1]]
        print(val, flower)
        plane[0][flower][val] = 1
        # print(plane)
    
    return plane

# plane = np.zeros((3,4,13), dtype= int) 
# hand = ['3-C', '4-D', '5-S', '6-H', '7-C', '8-C']
# print(encode_hand(plane,hand))

def encode_target(plane, target):
    
    '''
        Encode target and represerve it into plane

        plane (array): 1*4*13 numpy array
        target (str): string of target card

        Returns:
            (array): 1*4*13
    '''
    
    target_info = target.split('-')
    val = VAL_MAP[target_info[0]]
    flower = FlOWER_MAP[target_info[1]]
    plane[flower][val] = 1
    return plane

# plane = np.zeros((4,13), dtype= int) 
# target = '3-S'
# print(encode_target(plane,target))
