import pygame
import os
import sys
from constants import SQUARE_SIZE, FPS, WIN
from board import Board
from interface import Interface

pygame.init()
pygame.display.set_caption('Go by Gavril Marinov')
logo = pygame.image.load(os.path.join('src/images', 'go_icon.png'))
pygame.display.set_icon(logo)

# Transform mouse position into rows and columns of the board list
def get_row_col_mouse(pos):
    x, y = pos
    row = (y // SQUARE_SIZE)
    col = (x // SQUARE_SIZE)
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    interface = Interface()
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # If stone is placed on the board
                if 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count < 2:
                    row, col = get_row_col_mouse(pos)
                    if board.white_to_move == False:
                        placed_stone = board.black_stone
                        opponent_stone = board.white_stone
                    else:
                        placed_stone = board.white_stone
                        opponent_stone = board.black_stone
                    board.place_stone(row + 1, col + 1,
                                      placed_stone, opponent_stone)
                # If pass button is clicekd
                elif (interface.pos_x <= pos[0] <= interface.pos_x + 140 and
                      interface.b_pass_pos_y <= pos[1] <= interface.b_pass_pos_y + 40 and 
                      board.pass_count < 2 and board.white_to_move == False):
                    board.pass_move()
                elif (interface.pos_x <= pos[0] <= interface.pos_x + 140 and
                      interface.w_pass_pos_y <= pos[1] <= interface.w_pass_pos_y + 40 and 
                      board.pass_count < 2 and board.white_to_move == True):
                    board.pass_move()
                # If game has ended, mark the death stones
                elif 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count == 2:
                    row, col = get_row_col_mouse(pos)
                    board.remove_dead_stones(row + 1, col + 1, board.white_to_move)
                # If ready button is clicked (black)
                elif (interface.pos_x <= pos[0] <= interface.pos_x + interface.ready_width and 
                      interface.b_ready_pos_y <= pos[1] <= interface.b_ready_pos_y + 
                      interface.butt_height and board.pass_count == 2):
                    board.white_to_move = True
                # If ready button is clicked (white)
                elif (interface.pos_x <= pos[0] <= interface.pos_x + interface.ready_width and 
                      interface.w_ready_pos_y <= pos[1] <= interface.w_ready_pos_y + 
                      interface.butt_height and board.pass_count == 2):
                # If new game button is clicked
                    board.calc_score()
                elif (interface.pos_x <= pos[0] <= interface.pos_x + interface.new_game_width and 
                      interface.new_game_pos_y <= pos[1] <= interface.new_game_pos_y + 
                      interface.butt_height and board.game_end == True):
                    main()
                # If exit game button is clicked
                elif (interface.pos_x <= pos[0] <= interface.pos_x + interface.quit_width and 
                      interface.quit_pos_y <= pos[1] <= interface.quit_pos_y + interface.butt_height):
                    pygame.QUIT
                    sys.exit()
        board.draw_squares(WIN)
        board.draw_stones(WIN)
        if board.stone_placed == True:
            board.draw_circle(WIN, board.pos_x, board.pos_y, board.white_to_move)
        interface.draw_quit(WIN, pos)
        # Game in progress
        if board.pass_count < 2:
            interface.draw_players_turn(WIN, board.white_to_move)
            interface.draw_players_text(
            WIN, board.captued_white_stones, board.captued_black_stones)
            interface.draw_pass(WIN, pos, board.white_to_move)
            if board.start_time and pygame.time.get_ticks() - board.start_time < 600:
                interface.draw_inv_move(WIN)
        # Remove dead stones
        if board.pass_count == 2 and board.game_end == False:
            if board.remove_sound_check == True:
                board.remove_sound.play()
                board.remove_sound_check = False
            interface.draw_death_stones_msg(WIN, board.white_to_move)
            interface.draw_players_text(WIN, board.captued_white_stones, 
                                        board.captued_black_stones)
            interface.draw_ready(WIN, pos, board.white_to_move)
        # Final score
        if board.game_end == True:
            interface.draw_players_text(WIN, board.captued_white_stones, board.captued_black_stones)
            interface.draw_total_score(WIN, board.white_territory_count, board.captued_black_stones, 
                                       board.black_territory_count, board.captued_white_stones, board.komi)               
            interface.draw_new_game(WIN, pos)
        pygame.display.update()
main()