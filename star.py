from game.bordar import GameBordar
from game.player import RandomPlayer
from game.game import Game, QueuePlayers

def main():
    game = Game(RandomPlayer(name="pl-1"), RandomPlayer(name="pl-2"))

    while game.is_continues:
        game.segmentGame()
    game.bordar.art()





if __name__ == "__main__":
    main()