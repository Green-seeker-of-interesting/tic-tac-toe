from abc import ABC, abstractmethod
from random import choice
import typing as tp

import numpy as np
from keras.models import model_from_json

from .bordar import GameBordar


class Player(ABC):

    def __init__(self, name: str):
        self.name = name
        self.bordar_states = []
        self.wins = 0

    def remember_state(self, bordar: GameBordar, next_move: int):
        self.bordar_states.append([bordar.give_bordar_vector().copy(), next_move])

    def save(self):
        with open("games.csv", "a") as f:
            for state in self.bordar_states:
                if state[0][state[1]] == 0:  
                    for item in state[0]:
                        f.write(str(item) + ",")
                    f.write(str(state[1]) + "\n")
            

    @abstractmethod
    def next_move(self, bordar: GameBordar) -> int:
        pass

    @abstractmethod
    def end_game(self, is_vin: bool):
        pass


class RandomPlayer(Player):

    def next_move(self, bordar: GameBordar) -> int:
        available_moves = self.give_available_moves(bordar=bordar)
        next_move = choice(available_moves)
        self.remember_state(bordar, next_move)
        return next_move

    def give_available_moves(self, bordar: GameBordar) -> tp.List[int]:
        available_moves = []
        vek = bordar.give_bordar_vector()
        for i, el in enumerate(np.nditer(vek)):
            if el == 0:
                available_moves.append(i)
        return available_moves

    def end_game(self, is_vin: bool) -> None:
        if is_vin:
            self.wins += 1
            # self.save()
        self.bordar_startes = []


class AIPlayer(Player):

    def __init__(self, name: str):
        super().__init__(name)
        self.model = self.init_model()

    def init_model(self):
        with open('game/unit/' + self.name + '/model.json', 'r') as f:
            loaded_model = model_from_json(f.read())
        loaded_model.load_weights('game/unit/' + self.name + '/weights.h5')
        return loaded_model

    def next_move(self, bordar: GameBordar) -> int:
        vektor = np.array([bordar.give_bordar_vector()])
        move = self.model.predict(vektor,verbose=0)
        next_move = np.argmax(move)
        self.remember_state(bordar, next_move)
        return next_move

    def end_game(self, is_vin: bool):
        if is_vin:
            self.wins += 1
            # self.save()
        self.bordar_startes = []