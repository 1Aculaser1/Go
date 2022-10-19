import pygame
from constants import WIN

class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
        
class Text:
    def __init__(self, x, y, text, color, font):
        if font == 'font1':
            self.font = pygame.font.SysFont("Consolas", 28)
        elif font == 'font2':
            self.font = pygame.font.SysFont("Consolas", 28, bold=True)
        elif font == 'font3':
            self.font = pygame.font.SysFont("Consolas", 18)
        elif font == 'font4':
            self.font = pygame.font.SysFont("Consolas", 18, bold=True)
        self.x = x
        self.y = y
        self.text = self.font.render(text, True, color)
        self.draw_text()
    
    def draw_text(self):
        WIN.blit(self.text, (self.x, self.y))
    
