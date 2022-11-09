import numpy as np


class GameBordar:

    def __init__(self) -> None:
        self.tik = 0
        self.bordar = np.zeros(9, dtype=int)

    def make_move(self, move_index:int):
        if self.bordar[move_index] == 0:
            if self.tik % 2 == 0:
                self.bordar[move_index] = 1
            else:
                self.bordar[move_index] = -1
        self.tik += 1

    def art(self) -> None:
        print(f"{self.bordar[0]} {self.bordar[1]} {self.bordar[2]}")
        print(f"{self.bordar[3]} {self.bordar[4]} {self.bordar[5]}")
        print(f"{self.bordar[6]} {self.bordar[7]} {self.bordar[8]}")

    def give_bordar_vector(self) -> np.ndarray:
        if self.tik % 2 == 0:
            return self.bordar
        else:
            return self.invert_bordar()

    def invert_bordar(self) -> np.ndarray:
        out = np.zeros(9, dtype=int)
        for i, el in enumerate(self.bordar):
            if el == 1: 
                out[i] = -1
            elif el == -1:
                out[i] = 1
        return out
