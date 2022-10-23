import pygame
import os
from constants import WIN

# Images and Sounds
pygame.init()
title_text = "Go by Gavril Marinov"
main_logo = pygame.image.load(os.path.join("src/images", "main.png"))
board_img = pygame.image.load(os.path.join("src/images", "board.png"))
stone_sound = pygame.mixer.Sound(os.path.join("src/sounds", "place.wav"))
capture_sound = pygame.mixer.Sound(os.path.join("src/sounds", "capture_single.wav"))
capture_sound_m = pygame.mixer.Sound(os.path.join("src/sounds", "capture_many.wav"))
invalid_sound = pygame.mixer.Sound(os.path.join("src/sounds", "invalid.wav"))
pass_sound = pygame.mixer.Sound(os.path.join("src/sounds", "pass.wav"))
remove_sound = pygame.mixer.Sound(os.path.join("src/sounds", "remove.wav"))
black_wins_sound = pygame.mixer.Sound(os.path.join("src/sounds", "black_wins.wav"))
white_wins_sound = pygame.mixer.Sound(os.path.join("src/sounds", "white_wins.wav"))
logo = pygame.image.load(os.path.join("src/images", "go_icon.png"))

class Field:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

    def get_loc(self, p0, p1):
        if self.x <= p0 <= self.x + self.width and self.y <= p1 <= self.y + self.height:
            return True
        
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
