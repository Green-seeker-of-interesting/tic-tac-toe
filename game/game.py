from .bordar import GameBordar
from .player import Player


class Game:

    def __init__(self, player_1: Player, player_2: Player):
        self.bordar = GameBordar()
        self.player_1 = player_1
        self.player_2 = player_2

    def segmentGame(self):
        pass

    def _give_player(self):
        # TODO: в отдельный  микро клас 
        while True:
            yield self.player_1
            yield self.player_2

    
