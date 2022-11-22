import pygame
import random

# CONSTANTS
GREY = (155, 155, 155)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH, HEIGHT = 460, 390
SIZE = 30

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
        block = Block(0, 0, RED)
        while True:
            self.window.blit(self.background, (0, 0))
            block.draw(self.window)
            pygame.display.update()
            self.clock.tick(60)

    def make_background(self):
        background = pygame.Surface((WIDTH, HEIGHT))
        background.fill(GREY)
        pygame.draw.rect(background, BLACK, (0, 0, 300, HEIGHT))
        return background

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


if __name__ == "__main__":
    game = Game()
    game.run()