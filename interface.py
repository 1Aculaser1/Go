import pygame
from constants import DARK_GREY, LIGHT_GREY, WHITE, RED, GREEN

class Interface:
    def __init__(self):
        # Interface fonts
        self.int_font = pygame.font.SysFont('Consolas', 28)
        self.int_font2 = pygame.font.SysFont('Consolas', 18)
        self.int_font3 = pygame.font.SysFont('Consolas', 28, bold=True)
        # x position for pass, ready and players tab
        self.pos_x = 796
        # Pass button
        self.pass_width = 70
        self.pass_height = 40
        self.b_pass_pos_y = 100
        self.w_pass_pos_y = 427
        self.pass_text = self.int_font.render(
            'pass', True, WHITE)
        # Ready button
        self.ready_width = 85
        self.ready_height = 35
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
        self.inv_move_height = 35
        self.inv_move_pos_x = 282
        self.inv_move_pos_y = 367
        self.inv_move_txt = self.int_font3.render(
            'Invalid Move!', True, RED)
        # Death Stones message
        self.death_stones_width = 242
        self.death_stones_height = 92
        self.death_stones_pos_x = 775
        self.w_death_stones_pos_y = 100
        self.w_death_stones_txt_pos_y = 415
        self.b_death_stones_pos_y = 20
        self.b_death_stones_txt_pos_y = 88
        self.death_stones_txt = self.int_font2.render(
            'Remove the death stones', True, RED)

    def draw_pass(self, win, pos, turn):
        if turn == False:
            if (self.pos_x <= pos[0] <= self.pos_x + self.pass_width and self.b_pass_pos_y <= pos[1] <= self.b_pass_pos_y + self.pass_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x,
                                self.b_pass_pos_y, self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.b_pass_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x,
                                self.b_pass_pos_y, self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.b_pass_pos_y + 5))
        else:
            if (self.pos_x <= pos[0] <= self.pos_x + self.pass_width and self.w_pass_pos_y <= pos[1] <= self.w_pass_pos_y + self.pass_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x,
                                self.w_pass_pos_y, self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.w_pass_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x,
                                self.w_pass_pos_y, self.pass_width, self.pass_height))
                win.blit(self.pass_text, (self.pos_x + 5, self.w_pass_pos_y + 5))

    def draw_players_text(self, win, b_count, w_count):
        capture_count_b = self.int_font2.render(
            'Captured Stones: ' + str(b_count), True, WHITE)
        capture_count_w = self.int_font2.render(
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
                         self.inv_move_pos_y, self.inv_move_width, self.inv_move_height))
        win.blit(self.inv_move_txt,
                 (self.inv_move_pos_x + 5, self.inv_move_pos_y + 5))

    def draw_total_score(self, win, white_territory, captured_black_stones, black_territory, captured_white_stones, komi):
        total_score_w = self.int_font2.render(
            'Total Score: ' + str(white_territory + captured_black_stones + komi), True, WHITE)
        total_score_b = self.int_font2.render(
            'Total Score: ' + str(black_territory + captured_white_stones), True, WHITE)
        win.blit(total_score_w, (self.pos_x + 5, self.w_p_pos_y + 65))
        win.blit(total_score_b, (self.pos_x + 5, self.b_p_pos_y + 65))
        black_wins = self.int_font.render(
            'Black Wins!', True, GREEN)
        white_wins = self.int_font.render(
            'White Wins!', True, GREEN)
        if white_territory + captured_black_stones + komi > black_territory + captured_white_stones:
            win.blit(white_wins, (self.pos_x + 5, self.w_p_pos_y + 5))
        else:
            win.blit(black_wins, (self.pos_x + 5, self.b_p_pos_y + 5))

    def draw_death_stones_msg(self, win, turn):
        if turn == False:
            pygame.draw.rect(win, LIGHT_GREY, (self.death_stones_pos_x,
                             self.b_death_stones_pos_y, self.death_stones_width, self.death_stones_height))
            win.blit(self.death_stones_txt, (self.death_stones_pos_x +
                     5, self.b_death_stones_txt_pos_y))
        else:
            pygame.draw.rect(win, LIGHT_GREY, (self.death_stones_pos_x,
                             self.w_p_pos_y, self.death_stones_width, self.death_stones_height))
            win.blit(self.death_stones_txt, (self.death_stones_pos_x +
                     5, self.w_death_stones_txt_pos_y))

    def draw_ready(self, win, pos, turn):
        if turn == False:
            if (self.pos_x <= pos[0] <= self.pos_x + self.ready_width and self.b_ready_pos_y <= pos[1] <= self.b_ready_pos_y + self.ready_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x,
                                self.b_ready_pos_y, self.ready_width, self.ready_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.b_ready_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x,
                                self.b_ready_pos_y, self.ready_width, self.ready_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.b_ready_pos_y + 5))
        else:
            if (self.pos_x <= pos[0] <= self.pos_x + self.ready_width and self.w_ready_pos_y <= pos[1] <= self.w_ready_pos_y + self.ready_height):
                pygame.draw.rect(win, LIGHT_GREY, (self.pos_x,
                                self.w_ready_pos_y, self.ready_width, self.ready_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.w_ready_pos_y + 5))
            else:
                pygame.draw.rect(win, DARK_GREY, (self.pos_x,
                                self.w_ready_pos_y, self.ready_width, self.ready_height))
                win.blit(self.ready_text, (self.pos_x + 5, self.w_ready_pos_y + 5))