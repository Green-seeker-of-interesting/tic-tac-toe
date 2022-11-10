from random import choice

import pygame

from .boradr_view import viewBordar
from game.bordar import GameBordar
from game.player import RandomPlayer, AIPlayer
from game.game import Game

FPS = 30  # частота кадров в секунду


pygame.init()
pygame.display.set_caption("H_V")
clock = pygame.time.Clock()


def give_bordar_for_test() -> GameBordar:
    mas = [
        [2, 4, 6, 1, 3, 7],
        [2, 0, 5, 1, 4, 6, 8],
        [2, 8, 6, 0, 5, 1, 3, 7, 4],
        [6, 3, 0, 4, 8, 1, 5, 7],
        [2, 4, 6, 7, 5, 3, 0, 8, 1],
        [1, 5, 3, 7, 4, 6, 0, 8],
        [2, 6, 8, 5, 4, 7, 3, 1, 0],
        [0, 4, 6, 3, 8, 1, 7],
    ]
    out = GameBordar()
    for i in choice(mas):
        out.make_move(i)
    return out


def give_game():
    pl_ai = AIPlayer(name="exk3")
    pl_rd = RandomPlayer(name="rp_1")
    while True:
        pygame.display.set_caption(f"красный - {pl_ai.name}  |  синий - {pl_rd.name}")
        yield Game(pl_ai, pl_rd)
        pygame.display.set_caption(f"красный - {pl_rd.name}  |  синий - {pl_ai.name}")
        yield Game(pl_rd, pl_ai)


def running():
    running = True
    displey = viewBordar()
    GeneratorGame = give_game()
    game = next(GeneratorGame)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    if game.is_continues:
                        game.segmentGame()
                        displey.update(bordar=game.bordar)
                    else:
                        game = next(GeneratorGame)
                        displey.update(bordar=game.bordar)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
