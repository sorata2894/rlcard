
class SevensCard:

    info = {'type': ['number'],
        'val': ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'],
        'flower': ['c', 'd', 'h', 's']
    }

    def __init__(self, card_type, card_val, card_flower):
        
        '''Initialize the class of Sevens

        Args:
            card_type (str): The type of card
            flower (str): The flower of card
            val (str): the val trait of card
        '''
        
        self.type = card_type
        self.val = card_val
        self.flower = card_flower
        self.str = self.get_str()
    
    def get_str(self):
        
        '''
            Get the string representation of card of Sevens

            Return:
                (str): The string of card's val and flower
        '''

        return self.val + '-' + self.flower
    
    '''
        I have no idea how to print the card 
        so i won't code it right now
        i will leave the website right down hear
        https://github.com/datamllab/rlcard/blob/master/rlcard/games/uno/card.py
    '''

    @staticmethod
    def print_cards(cards):
        pass

