winner = []
min_coverpoint = []
def find_smallest(players):
    min_coverpoint.append(players[0].coverpoint,players[1].coverpoint,players[2].coverpoint,players[3].coverpoint)
    a = min(min_coverpoint)
    return min_coverpoint.index(a)

class SevensJudger:
    @staticmethod
    def judge_winner(players):
            
        '''
            Judge the winner of the game

            Args:
                players (list): The list of players who play the game

            Returns:
                (list): The player id of the winner
        '''

        count_1 = len(players[0].hand)
        count_2 = len(players[1].hand)
        count_3 = len(players[2].hand)
        count_4 = len(players[3].hand)

        if count_1 == 0 and count_2 == 0 and count_3 == 0 and count_4 == 0:
            if len(players[0].cover) == 13 or len(players[1].cover) == 13 or len(players[2].cover) == 13 or len(players[3].cover) == 13:
                if len(players[0].cover) == 13:
                    winner.append(0)
                if len(players[1].cover) == 13:
                    winner.append(1)
                if len(players[2].cover) == 13:
                    winner.append(2)
                if len(players[3].cover) == 13:
                    winner.append(3)
                return True, winner
            else:
                return True, find_smallest(players)
        else:
            return False

    
            


