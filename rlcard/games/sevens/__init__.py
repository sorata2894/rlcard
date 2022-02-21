import sys
import os
sys.path.append(os.path.abspath("D:\\rlcard\\rlcard\\games\\sevens"))

from dealer import SevensDealer as Dealer
from judger import SevensJudger as Judger
from player import SevensPlayer as Player
from round  import SevensRound  as Round
from game   import SevensGame   as Game 

# from rlcard.games.sevens.dealer import SevensDealer as Dealer
# from rlcard.games.sevens.judger import SevensJudger as Judger
# from rlcard.games.sevens.player import SevensPlayer as Player
# from rlcard.games.sevens.round import SevensRound as Round
# from rlcard.games.sevens.game import SevensGame as Game