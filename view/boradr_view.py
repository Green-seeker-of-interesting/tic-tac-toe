import pygame

from game.bordar import GameBordar

CELL_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class viewBordar:

    def __init__(self):
        self.screen = pygame.display.set_mode((CELL_SIZE*3, CELL_SIZE*3))
        self.background_color = WHITE

    def update(self, bordar: GameBordar):
        self.screen.fill(self.background_color)
        self.grid()
        self.chips(bordar=bordar)

    def grid(self):
        # Вертикальная сетка
        pygame.draw.line(self.screen, start_pos=(CELL_SIZE, 0), end_pos=(
            CELL_SIZE, 3*CELL_SIZE), color=BLACK)
        pygame.draw.line(self.screen, start_pos=(CELL_SIZE*2, 0), end_pos=(
            CELL_SIZE*2, 3*CELL_SIZE), color=BLACK)

        # Горизонтальная сетка
        pygame.draw.line(self.screen, start_pos=(0, CELL_SIZE), end_pos=(
            3*CELL_SIZE, CELL_SIZE), color=BLACK)
        pygame.draw.line(self.screen, start_pos=(0, CELL_SIZE*2), end_pos=(
            3*CELL_SIZE, CELL_SIZE*2), color=BLACK)

    def chips(self, bordar: GameBordar):
        bord = bordar._bordar
        for i, val in enumerate(bord):
            if val == 1:
                self.art_chip(RED,i)
            elif val == -1:
                self.art_chip(BLUE,i)

    def art_chip(self, color:tuple, index: int):
        shifts = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1),
            (2, 1), (0, 2), (1, 2), (2, 2)]
        pygame.draw.rect(self.screen, color,
                    (shifts[index][0] * CELL_SIZE + 10, 
                    shifts[index][1] * CELL_SIZE + 10, 
                    CELL_SIZE - 20, CELL_SIZE - 20))
