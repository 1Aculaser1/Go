import pygame
import os
from constants import DARK_GREY, LIGHT_GREY, WHITE, RED, GREEN

class Interface:
    def __init__(self):
        # Interface fonts
        self.int_font = pygame.font.SysFont('Consolas', 28)
        self.int_font2 = pygame.font.SysFont('Consolas', 28, bold=True)
        self.int_font3 = pygame.font.SysFont('Consolas', 18)
        self.int_font4 = pygame.font.SysFont('Consolas', 18, bold=True)
        # x position for the interface buttons
        self.pos_x = 796
        # Button height
        self.butt_height = 35
        # Pass button
        self.pass_width = 70
        self.pass_height = 40
        self.b_pass_pos_y = 100
        self.w_pass_pos_y = 427
        self.pass_text = self.int_font.render(
            'pass', True, WHITE)
        # Ready button
        self.ready_width = 85
        self.b_ready_pos_y = 124
        self.w_ready_pos_y = 454
        self.ready_text = self.int_font.render(
            'Ready', True, WHITE)
        # Players tab
        self.p_width = 200
        self.p_height = 65
        self.b_p_pos_y = 23
        self.b_p_txt = self.int_font.render(
            'Black', True, WHITE)
        self.w_p_pos_y = 350
        self.w_p_txt = self.int_font.render(
            'White', True, WHITE)
        # Invalid move
        self.inv_move_width = 201
        self.inv_move_pos_x = 282
        self.inv_move_pos_y = 367
        self.inv_move_txt = self.int_font2.render(
            'Invalid Move!', True, RED)
        # Death Stones message
        self.death_stones_width = 242
        self.death_stones_height = 92
        self.death_stones_pos_x = 775
        self.w_death_stones_pos_y = 100
        self.w_death_stones_txt_pos_y = 415
        self.b_death_stones_pos_y = 20
        self.b_death_stones_txt_pos_y = 88
        self.death_stones_txt = self.int_font3.render(
            'Remove the death stones', True, RED)
        # New Game
        self.new_game_width = 130
        self.new_game_pos_y = 607
        self.new_game_text = self.int_font2.render(
            'New Game', True, WHITE)
        # Quit
        self.quit_width = 144
        self.quit_pos_y = 650
        self.quit_text = self.int_font2.render(
            'Exit Game', True, WHITE)
        # Win sound
        self.win_sound_check = True
        self.black_wins_sound = pygame.mixer.Sound(os.path.join('src/sounds', 'black_wins.wav'))
        self.white_wins_sound = pygame.mixer.Sound(os.path.join('src/sounds', 'white_wins.wav'))

    def draw_pass(self, win, pos, turn):
        if turn == False:
            if (self.pos_x <= pos[0] <= self.pos_x + self.pass_width and
                self.b_pass_pos_y <= pos[1] <= self.b_pass_pos_y + self.pass_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x, self.b_pass_pos_y, 
                                                   self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.b_pass_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x, self.b_pass_pos_y, 
                                                  self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.b_pass_pos_y + 5))
        else:
            if (self.pos_x <= pos[0] <= self.pos_x + self.pass_width and 
                self.w_pass_pos_y <= pos[1] <= self.w_pass_pos_y + self.pass_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x, self.w_pass_pos_y, 
                                                   self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.w_pass_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x, self.w_pass_pos_y, 
                                                  self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.w_pass_pos_y + 5))

    def draw_players_text(self, win, b_count, w_count):
        capture_count_b = self.int_font3.render(
            'Captured Stones: ' + str(b_count), True, WHITE)
        capture_count_w = self.int_font3.render(
            'Captured Stones: ' + str(w_count), True, WHITE)
        win.blit(self.b_p_txt,
                 (self.pos_x + 5, self.b_p_pos_y + 5))
        win.blit(capture_count_b, (self.pos_x +
                 5, self.b_p_pos_y + 40))
        win.blit(self.w_p_txt,
                 (self.pos_x + 5, self.w_p_pos_y + 5))
        win.blit(capture_count_w, (self.pos_x +
                 5, self.w_p_pos_y + 40))

    def draw_players_turn(self, win, turn):
        if turn == False:
            pygame.draw.rect(win, LIGHT_GREY, (self.pos_x,
                             self.b_p_pos_y, self.p_width, self.p_height))
        else:
            pygame.draw.rect(win, LIGHT_GREY, (self.pos_x,
                             self.w_p_pos_y, self.p_width, self.p_height))

    def draw_inv_move(self, win):
        pygame.draw.rect(win, LIGHT_GREY, (self.inv_move_pos_x,
                         self.inv_move_pos_y, self.inv_move_width, self.butt_height))
        win.blit(self.inv_move_txt,
                (self.inv_move_pos_x + 5, self.inv_move_pos_y + 5))

    def draw_total_score(self, win, white_territory, captured_black_stones, 
                         black_territory, captured_white_stones, komi):
        white_territory_txt = self.int_font3.render(
            'Territory: ' + str(white_territory), True, WHITE)
        black_territory_txt = self.int_font3.render(
            'Territory: ' + str(black_territory), True, WHITE)
        komi_txt = self.int_font3.render(
            'Komi: 6.5', True, WHITE)
        total_score_w = self.int_font4.render(
            'Total Score: ' + str(white_territory + captured_black_stones + komi), True, WHITE)
        total_score_b = self.int_font4.render(
            'Total Score: ' + str(black_territory + captured_white_stones), True, WHITE)
        win.blit(black_territory_txt, (self.pos_x + 5, self.b_p_pos_y + 65))
        win.blit(total_score_b, (self.pos_x + 5, self.b_p_pos_y + 90))
        win.blit(white_territory_txt, (self.pos_x + 5, self.w_p_pos_y + 65))
        win.blit(komi_txt, (self.pos_x + 5, self.w_p_pos_y + 89))
        win.blit(total_score_w, (self.pos_x + 5, self.w_p_pos_y + 114))
        black_wins = self.int_font.render(
            'Black Wins!', True, GREEN)
        white_wins = self.int_font.render(
            'White Wins!', True, GREEN)
        if white_territory + captured_black_stones + komi > black_territory + captured_white_stones:
            win.blit(white_wins, (self.pos_x + 5, self.w_p_pos_y + 5))
            if self.win_sound_check == True:
                self.white_wins_sound.play()
        else:
            win.blit(black_wins, (self.pos_x + 5, self.b_p_pos_y + 5))
            if self.win_sound_check == True:
                self.black_wins_sound.play()
        self.win_sound_check = False

    def draw_death_stones_msg(self, win, turn):
        if turn == False:
            pygame.draw.rect(win, LIGHT_GREY, (self.death_stones_pos_x, self.b_death_stones_pos_y, 
                                               self.death_stones_width, self.death_stones_height))
            win.blit(self.death_stones_txt, (self.death_stones_pos_x +5, self.b_death_stones_txt_pos_y))
        else:
            pygame.draw.rect(win, LIGHT_GREY, (self.death_stones_pos_x, self.w_p_pos_y, 
                                               self.death_stones_width, self.death_stones_height))
            win.blit(self.death_stones_txt, (self.death_stones_pos_x +5, self.w_death_stones_txt_pos_y))

    def draw_ready(self, win, pos, turn):
        if turn == False:
            if (self.pos_x <= pos[0] <= self.pos_x + self.ready_width and 
                self.b_ready_pos_y <= pos[1] <= self.b_ready_pos_y + self.butt_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x, self.b_ready_pos_y, 
                                                   self.ready_width, self.butt_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.b_ready_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x, self.b_ready_pos_y, 
                                                  self.ready_width, self.butt_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.b_ready_pos_y + 5))
        else:
            if (self.pos_x <= pos[0] <= self.pos_x + self.ready_width and 
                self.w_ready_pos_y <= pos[1] <= self.w_ready_pos_y + self.butt_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x, self.w_ready_pos_y, 
                                                   self.ready_width, self.butt_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.w_ready_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x, self.w_ready_pos_y, 
                                                  self.ready_width, self.butt_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.w_ready_pos_y + 5))

    def draw_new_game(self, win, pos):
        if (self.pos_x <= pos[0] <= self.pos_x + self.new_game_width and 
            self.new_game_pos_y <= pos[1] <= self.new_game_pos_y + self.butt_height):
            pygame.draw.rect(win, LIGHT_GREY, (self.pos_x, self.new_game_pos_y, 
                                               self.new_game_width, self.butt_height))
            win.blit(self.new_game_text, (self.pos_x + 5, self.new_game_pos_y + 5))
        else:
            pygame.draw.rect(win, DARK_GREY, (self.pos_x, self.new_game_pos_y, 
                                              self.new_game_width, self.butt_height))
            win.blit(self.new_game_text, (self.pos_x + 5, self.new_game_pos_y + 5))

    def draw_quit(self, win, pos):
        if (self.pos_x <= pos[0] <= self.pos_x + self.quit_width and 
            self.quit_pos_y <= pos[1] <= self.quit_pos_y + self.butt_height):
            pygame.draw.rect(win, LIGHT_GREY, (self.pos_x, self.quit_pos_y, 
                                               self.quit_width, self.butt_height))
            win.blit(self.quit_text, (self.pos_x + 5, self.quit_pos_y + 5))
        else:
            pygame.draw.rect(win, DARK_GREY, (self.pos_x, self.quit_pos_y, 
                                              self.quit_width, self.butt_height))
            win.blit(self.quit_text, (self.pos_x + 5, self.quit_pos_y + 5))