import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid: Grid = []

        for _ in range(self.rows):
            if randomize:
                row = [random.randint(0, 1) for _ in range(self.cols)]
            else:
                row = [0 for _ in range(self.cols)]
            grid.append(row)

        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        x, y = cell
        neighbours = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x, y) != (x + i, y + j):
                    new_x, new_y = x + i, y + j
                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        neighbours.append(self.curr_generation[new_x][new_y])

        return neighbours

    def get_next_generation(self) -> Grid:
        new_gen = self.create_grid(False)
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                neighbours = self.get_neighbours((x, y))
                if self.curr_generation[x][y] and 2 <= sum(neighbours) <= 3:
                    new_gen[x][y] = 1
                elif not self.curr_generation[x][y] and sum(neighbours) == 3:
                    new_gen[x][y] = 1
        self.generations += 1
        return new_gen

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if not self.max_generations:
            return False
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r", encoding="UTF-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        grid: Grid = [[int(c) for c in line] for line in lines]

        rows = len(grid)
        cols = len(grid[0])

        game = GameOfLife(size=(rows, cols), randomize=False)
        game.curr_generation = grid
        game.prev_generation = game.create_grid(randomize=False)

        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding="UTF-8") as f:
            for row in self.curr_generation:
                f.write("".join(map(str, row)) + "\n")
