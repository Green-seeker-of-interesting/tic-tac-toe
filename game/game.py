from .bordar import GameBordar
from .player import Player


class Game:

    def __init__(self, player_1: Player, player_2: Player):
        self.bordar = GameBordar()
        self.queue = QueuePlayers(player_1, player_2).give_generator()
        self.is_continues = True
        self.move_history = []

    def segmentGame(self):  # не очевидный момент
        player = next(self.queue)
        next_move = player.next_move(self.bordar)
        self.move_history.append(str(int(next_move)))
        self.bordar.make_move(next_move)

        if self.is_end_game():
            player.end_game(is_vin=True)
            next(self.queue).end_game(is_vin=False)
            self.is_continues = False

        elif self.bordar._tik == 9:
            player.end_game(is_vin=False)
            next(self.queue).end_game(is_vin=False)
            self.is_continues = False

        return self.is_continues

    def is_end_game(self) -> bool:
        victory_options = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                           [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                           [2, 4, 6], [0, 4, 8]]
        bordar_vektor = self.bordar.give_bordar_vector()

        for option in victory_options:
            if bordar_vektor[option[0]] == bordar_vektor[option[1]] == bordar_vektor[option[2]] \
                    and bordar_vektor[option[0]] != 0:
                return True
        return False

    def save(self):
        with open("moves.csv", "a") as f:
            f.write(",".join(self.move_history) + "\n")


class QueuePlayers:

    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.player_1 = player_1
        self.player_2 = player_2

    def give_generator(self):
        while True:
            yield self.player_1
            yield self.player_2
