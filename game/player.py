from abc import ABC, abstractmethod
from random import choice

import numpy as np

from .bordar import GameBordar


class Player(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def next_move(self, bordar: GameBordar) -> int:
        pass

    @abstractmethod
    def end_game(self, is_vin: bool):
        pass


class RandomPlayer(Player):

    def next_move(self, bordar: GameBordar) -> int:
        available_moves = []
        vek = bordar.give_bordar_vector()
        for i, el in enumerate(np.nditer(vek)):
            if el == 0:
                available_moves.append(i)
        print(available_moves)
        return choice(available_moves)

    def end_game(self, is_vin: bool) -> None:
        print("Игра окончена")
