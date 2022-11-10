import numpy as np


class GameBordar:

    def __init__(self) -> None:
        self._tik = 0
        self._bordar = np.zeros(9, dtype=int)

    def make_move(self, move_index:int):
        if self._bordar[move_index] == 0:
            if self._tik % 2 == 0:
                self._bordar[move_index] = 1
            else:
                self._bordar[move_index] = -1
        self._tik += 1

    def art(self) -> None:
        print(f"{self._bordar[0]} {self._bordar[1]} {self._bordar[2]}")
        print(f"{self._bordar[3]} {self._bordar[4]} {self._bordar[5]}")
        print(f"{self._bordar[6]} {self._bordar[7]} {self._bordar[8]}")

    def give_bordar_vector(self) -> np.ndarray:
        if self._tik % 2 == 0:
            return self._bordar
        else:
            return self._invert_bordar()

    def _invert_bordar(self) -> np.ndarray:
        out = np.zeros(9, dtype=int)
        for i, el in enumerate(self._bordar):
            if el == 1: 
                out[i] = -1
            elif el == -1:
                out[i] = 1
        return out
