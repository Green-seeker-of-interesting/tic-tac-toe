import os

from game.bordar import GameBordar
from game.player import RandomPlayer, AIPlayer, Player
from game.game import Game, QueuePlayers


def write_itog(pl_1: Player, pl_2: Player):
    os.system('clear')
    print(f"{pl_1.name} -> {pl_1.wins}")
    print(f"{pl_2.name} -> {pl_2.wins}")

    

def main():
    pl_ai = AIPlayer(name="m4")
    # pl_ai = RandomPlayer(name="rp_2")
    # pl_rd = RandomPlayer(name="rp_1")
    pl_rd = AIPlayer(name="m3")


    os.system('clear')
    
    for i in range(100):
        game = Game(pl_ai, pl_rd)
        while game.is_continues:
            game.segmentGame()
        
        game = Game(pl_rd, pl_ai)
        while game.is_continues:
            game.segmentGame()

    write_itog(pl_1=pl_ai, pl_2=pl_rd)



    




if __name__ == "__main__":
    main()