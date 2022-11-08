from game.bordar import GameBordar
from game.player import RandomPlayer
from game.game import Game

def main():
    game = Game(RandomPlayer(name='pl-1'), RandomPlayer(name='pl-2'))
    gen = game._give_player()
    for _ in range(10):
        print(next(gen).name)






if __name__ == "__main__":
    main()