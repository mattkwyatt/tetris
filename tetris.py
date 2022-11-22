import pygame
import random

# CONSTANTS
GREY = (155, 155, 155)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
COLOURS = [RED, GREEN]
WIDTH, HEIGHT = 460, 390
SIZE = 30
O = [(1, 0), (0, 0), (0, 1), (1, 1)]
I = [(-1, 0), (0, 0), (1, 0), (2, 0)]
T = [(-1, 0), (0, 0), (1, 0), (0, 1)]
L = [(-1, 0), (0, 0), (1, 0), (1, 1)]
SHAPES = [O, I, T, L]

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        self.font = pygame.font.SysFont("arial", 40)
        self.clock = pygame.time.Clock()
        self.background = self.make_background()
        random.seed()

    def run(self):
        timer = 0
        shape = Shape(4, 1)
        while True:
            timer += 1
            if timer % 60 == 0:
                self.drop(shape)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        shape.rotate()

            self.window.blit(self.background, (0, 0))
            for block in shape.design:
                block.draw(self.window)
            pygame.display.update()
            self.clock.tick(60)

    def make_background(self):
        background = pygame.Surface((WIDTH, HEIGHT))
        background.fill(GREY)
        pygame.draw.rect(background, BLACK, (0, 0, 300, HEIGHT))
        return background

    def drop(self, shape):
        for block in shape.design:
            block.row += 1

class Block:
    def __init__(self, column: int, row: int, colour: tuple[int, int, int]) -> None:
        self.column = column
        self.row = row
        self.colour = colour
        self.image = self.make_image(colour)

    def make_image(self, colour: tuple[int, int, int]):
        image = pygame.Surface((SIZE, SIZE))
        pygame.draw.rect(image, colour, (0, 0, SIZE, SIZE), 0)
        pygame.draw.rect(image, BLACK, (0, 0, SIZE, SIZE), 1)
        return image

    def draw(self, window: pygame.Surface):
        draw_pos = (SIZE * self.column, SIZE * self.row)
        window.blit(self.image, draw_pos)

    def move(self, column: int, row: int):
        self.column = column
        self.row = row

class Shape:
    def __init__(self, column: int, row: int) -> None:
        self.colour = random.choice(COLOURS)
        self.design = self.get_design(column, row)
        self.rotation = 1

    def get_design(self, column: int, row: int):
        self.design_style = random.choice(SHAPES)
        return [Block(column + b[0], row + b[1], self.colour) for b in self.design_style]

    def rotate(self):
        if self.design_style == O:
            return
        if self.design_style == I:
            self.rotation *= -1

        pivot = self.design[1]
        for square in self.design:
            if square != pivot:
                square.column -= pivot.column
                square.row -= pivot.row

                square.column, square.row = -self.rotation * square.row, self.rotation * square.column

                square.column += pivot.column
                square.row += pivot.row


if __name__ == "__main__":
    game = Game()
    game.run()