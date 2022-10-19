import pygame
from constants import SQUARE_SIZE, RED


class Stone:
    def __init__(self, row, col, color):
        self.row = row - 1  # - 1 because the ending rows/colums are 1 and not playable
        self.col = col - 1  # - 1 because the ending rows/colums are 1 and not playable
        self.color = color
        self.x = SQUARE_SIZE * (self.col) + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * (self.row) + SQUARE_SIZE // 2
        self.fonts = pygame.font.SysFont("Consolas", 28)
        self.cross_txt = self.fonts.render("x", True, RED)

    def draw_stone(self, win):
        pygame.draw.circle(win, self.color, (self.x + 4, self.y + 4), 19)

    def draw_territory(self, win):
        pygame.draw.rect(win, self.color, (self.x - 4, self.y - 4, 16, 16))

    def draw_cross(self, win):
        win.blit(self.cross_txt, (self.x - 4, self.y - 10))
