import pygame
import sys
from constants import SQUARE_SIZE, FPS, WIN, DARK_WHITE, BLACK, WHITE, DARK_GREY, LIGHT_GREY, RED, GREEN
from board import Board
from interface import *
from stones import Stone

pygame.display.set_caption(title_text)
pygame.display.set_icon(logo)
new_game = False
handicap = 0
komi = 6.5
image_sel = 0

# Transform mouse position into rows and columns of the board list
def get_row_col_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    global new_game, komi, handicap, image_sel
    settings = False
    run = True
    play_win_sound = True
    clock = pygame.time.Clock()
    board = Board(image_sel)
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        row, col = get_row_col_mouse(pos)

        # Draw game elements
        WIN.fill(DARK_GREY)
        if image_sel == 0:
            WIN.blit(main_logo, (0, 0))
        elif image_sel == 1:
            WIN.blit(main_logo1, (0, 0))
        else:
            WIN.blit(main_logo2, (0, 0))
        if new_game == True:
            board.draw_squares(WIN)
            if board.handicap_set != True:
                board.set_handicap(handicap)
            # Show the stone at mouse cursor
            if 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count < 2:
                if board.white_to_move == False:
                    stone = Stone(row + 1, col + 1, BLACK)
                    stone.draw_stone(WIN)
                else:
                    stone = Stone(row + 1, col + 1, DARK_WHITE)
                    stone.draw_stone(WIN)
            # Draw Stones
            board.draw_stones(WIN)
            # Draw a circle for the last played stone
            if board.stone_placed == True and board.pass_count < 1:
                board.draw_circle(WIN, board.pos_x, board.pos_y, board.white_to_move)
            # Draw pass button and turn markup
            if board.pass_count < 2 and board.white_to_move == False:
                turn_b = Field(796, 23, 200, 65, LIGHT_GREY)
                if 796 <= pos[0] <= 796 + 70 and 100 <= pos[1] <= 100 + 40:
                    pass_b = Field(796, 100, 70, 40, LIGHT_GREY)
                else:
                    pass_b = Field(796, 100, 70, 40, DARK_GREY)
                pass_b_txt = Text(801, 105, 'pass', WHITE, 'font1')
            elif board.pass_count < 2 and board.white_to_move == True:
                turn_b = Field(796, 350, 200, 88, LIGHT_GREY)
                if 796 <= pos[0] <= 796 + 70 and 450 <= pos[1] <= 450 + 40:
                    pass_b = Field(796, 450, 70, 40, LIGHT_GREY)
                else:
                    pass_b = Field(796, 450, 70, 40, DARK_GREY)
                pass_b_txt = Text(801, 455, 'pass', WHITE, 'font1')
            # Draw invalid move
            if board.start_time and pygame.time.get_ticks() - board.start_time < 600:
                inv_move_b = Field(282, 367, 201, 35, LIGHT_GREY)
                inv_move_txt = Text(287, 372, 'Invalid Move!', RED, 'font2')
            # Draw remove dead stones menu
            if board.pass_count == 2 and board.game_end == False:
                if board.remove_sound_check == True:
                    remove_sound.play()
                    board.remove_sound_check = False
                if board.white_to_move == False:
                    remove_highlight = Field(775, 20, 242, 92, LIGHT_GREY)
                    remove_txt = Text(780, 88, 'Remove the death stones', RED, 'font3')
                    if 796 <= pos[0] <= 796 + 85 and 124 <= pos[1] <= 124 + 35:
                        ready_b = Field(796, 124, 85, 35, LIGHT_GREY)
                    else:
                        ready_b = Field(796, 124, 85, 35, DARK_GREY)
                    ready_txt = Text(801, 129, 'Ready', WHITE, 'font1')
                else:
                    remove_highlight = Field(775, 350, 242, 115, LIGHT_GREY)
                    remove_txt = Text(780, 440, 'Remove the death stones', RED, 'font3')
                    if 796 <= pos[0] <= 796 + 85 and 475 <= pos[1] <= 475 + 35:
                        ready_b = Field(796, 475, 85, 35, LIGHT_GREY)
                    else:
                        ready_b = Field(796, 475, 85, 35, DARK_GREY)
                    ready_txt = Text(801, 480, 'Ready', WHITE, 'font1')
            # Draw final score
            if board.game_end == True:
                black_territory_txt = Text(801, 88, 'Territory: '
                + str(board.black_territory_count), WHITE, 'font3')
                black_total_score_txt = Text(801, 113, 'Total Score: '
                + str(board.black_territory_count + board.captued_white_stones), WHITE, 'font4')
                white_territory_txt = Text(801, 439, 'Territory: '
                + str(board.white_territory_count), WHITE, 'font3')
                white_total_score_txt = Text(801, 464, 'Total Score: '
                + str(board.white_territory_count + board.captued_black_stones + komi), WHITE, 'font4')
                if (board.white_territory_count + board.captued_black_stones + komi >
                    board.black_territory_count + board.captued_white_stones):
                    wins_txt = Text(801, 355, 'White Wins!', GREEN, 'font1')
                    if play_win_sound == True:
                        white_wins_sound.play()
                else:
                    wins_txt = Text(801, 28, 'Black Wins!', GREEN, 'font1')
                    if play_win_sound == True:
                        black_wins_sound.play()
                play_win_sound = False
            # Draw players text
            black_player = Text(801, 28, 'Black', WHITE, 'font1')
            capture_count_b = Text(801, 63, 'Captured Stones: ' + str(board.captued_white_stones), WHITE, 'font3')
            white_player = Text(801, 355, 'White', WHITE, 'font1')
            komi_txt = Text(801, 415, f'Komi: {komi}', WHITE, 'font3')
            capture_count_w = Text(801, 390, 'Captured Stones: ' + str(board.captued_black_stones), WHITE, 'font3')
            # Draw Exit Game
            if 796 <= pos[0] <= 796 + 146 and 693 <= pos[1] <= 693 + 35:
                exit_game_b = Field(796, 693, 146, 35, LIGHT_GREY)
            else:
                exit_game_b = Field(796, 693, 146, 35, DARK_GREY)
            exit_game_txt = Text(801, 698, 'Exit Game', WHITE, 'font2')
        elif new_game == False and settings == False:
            # Draw New Game
            if 796 <= pos[0] <= 796 + 130 and 607 <= pos[1] <= 607 + 35:
                new_game_b = Field(796, 607, 130, 35, LIGHT_GREY)
            else:
                new_game_b = Field(796, 607, 130, 35, DARK_GREY)
            new_game_txt = Text(801, 612, 'New Game', WHITE, 'font2')
            # Draw Settings
            if 796 <= pos[0] <= 796 + 130 and 650 <= pos[1] <= 650 + 35:
                settings_b = Field(796, 650, 130, 35, LIGHT_GREY)
            else:
                settings_b = Field(796, 650, 130, 35, DARK_GREY)
            settings_txt = Text(801, 655, 'Settings', WHITE, 'font2')
            # Draw Quit
            if 796 <= pos[0] <= 796 + 70 and 693 <= pos[1] <= 693 + 35:
                quit_b = Field(796, 693, 70, 35, LIGHT_GREY)
            else: 
                quit_b = Field(796, 693, 70, 35, DARK_GREY)
            quit_txt = Text(801, 698, 'Quit', WHITE, 'font2')
        elif new_game == False and settings == True:
            # Draw OK
            if 796 <= pos[0] <= 796 + 40 and 693 <= pos[1] <= 693 + 35:
                ok_b = Field(796, 693, 40, 35, LIGHT_GREY)
            else:
                ok_b = Field(796, 693, 40, 35, DARK_GREY)
            ok_txt = Text(801, 698, 'OK', WHITE, 'font2')
            # Draw Komi Settings
            if 936 <= pos[0] <= 936 + 20 and 649 <= pos[1] <= 649 + 20:
                komi_up_b = Field(936, 649, 20, 20, LIGHT_GREY)
            else:
                komi_up_b = Field(936, 649, 20, 20, DARK_GREY)
            if 857 <= pos[0] <= 857 + 20 and 649 <= pos[1] <= 649 + 20:
                komi_down_b = Field(857, 649, 20, 20, LIGHT_GREY)
            else:
                komi_down_b = Field(857, 649, 20, 20, DARK_GREY)
            komi_txt = Text(801, 650, f'Komi: <  {komi}  >', WHITE, 'font3')
            # Draw Handicap Settings
            if 956 <= pos[0] <= 956 + 20 and 624 <= pos[1] <= 624 + 20:
                hand_up_b = Field(956, 624, 20, 20, LIGHT_GREY)
            else:
                hand_up_b = Field(920, 624, 20, 20, DARK_GREY)
            if 897 <= pos[0] <= 897 + 20 and 624 <= pos[1] <= 624 + 20:
                hand_down_b = Field(897, 624, 20, 20, LIGHT_GREY)
            else:
                hand_down_b = Field(897, 624, 20, 20, DARK_GREY)
            hand_txt = Text(801, 625, f'Handicap: <  {handicap}  >', WHITE, 'font3')
            # Draw Background settings
            board_txt = Text(801, 30, f'Board:', WHITE, 'font3')
            if image_sel == 0:
                board_prev_highlight = Field(797, 54, 108, 108, RED)
            elif image_sel == 1:
                board_prev_highlight = Field(797, 171, 108, 108, RED)
            else:
                board_prev_highlight = Field(797, 288, 108, 108, RED)
            # Draw board preview images in Settings
            WIN.blit(board_prev, (801, 58))
            WIN.blit(board_prev1, (801, 175))
            WIN.blit(board_prev2, (801, 292))

        # In-Game Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if new_game == False and settings == False:
                    # If New Game button is clicked
                    if new_game_b.get_loc(pos[0], pos[1]): # type: ignore
                        new_game = True
                        main()
                    # If settings button is clicked
                    elif settings_b.get_loc(pos[0], pos[1]): # type: ignore
                        settings = True
                        break
                    # If quit button is clicked
                    elif quit_b.get_loc(pos[0], pos[1]): # type: ignore
                        pygame.QUIT
                        sys.exit()
                elif new_game == True and settings == False:
                    # If stone is placed on the board
                    if 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count < 2:
                        if board.white_to_move == False:
                            placed_stone = board.black_stone
                            opponent_stone = board.white_stone
                        else:
                            placed_stone = board.white_stone
                            opponent_stone = board.black_stone
                        board.place_stone(row + 1, col + 1, placed_stone, opponent_stone)
                    # If pass button is clicked
                    elif pass_b.get_loc(pos[0], pos[1]) and board.pass_count < 2: # type: ignore
                        board.pass_move()
                    # If a stone is clicked during removal phase
                    elif 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count == 2:
                        board.remove_dead_stones(row + 1, col + 1, board.white_to_move)
                    # If ready button is clicked (black)
                    elif (board.pass_count == 2 and 
                        board.white_to_move == False and 
                        ready_b.get_loc(pos[0], pos[1])): # type: ignore
                        board.white_to_move = True
                    # If ready button is clicked (white)
                    elif (board.pass_count == 2 and 
                        board.white_to_move == True and 
                        ready_b.get_loc(pos[0], pos[1])): # type: ignore
                        board.calc_score()
                    elif exit_game_b.get_loc(pos[0], pos[1]): # type: ignore
                        new_game = False
                elif settings == True:
                    # If board preview 1 is clicked
                    if 801 <= pos[0] <= 801 + 100 and 58 <= pos[1] <= 58 + 100:
                        image_sel = 0
                    # If board preview 2 is clicked
                    elif 801 <= pos[0] <= 801 + 100 and 175 <= pos[1] <= 175 + 100:
                        image_sel = 1
                    # If board preview 3 is clicked
                    elif 801 <= pos[0] <= 801 + 100 and 292 <= pos[1] <= 292 + 100:
                        image_sel = 2
                    # If OK button is clicked
                    elif ok_b.get_loc(pos[0], pos[1]): # type: ignore
                        settings = False
                    # If Komi button is clicked
                    elif komi_up_b.get_loc(pos[0], pos[1]): # type: ignore
                        komi += 1
                    elif komi_down_b.get_loc(pos[0], pos[1]) and komi != 0.5: # type: ignore
                        komi -= 1
                    # If Handicap button is clocked
                    elif hand_up_b.get_loc(pos[0], pos[1]) and handicap != 9: # type: ignore
                        handicap += 1
                    elif hand_down_b.get_loc(pos[0], pos[1]) and handicap != 0: # type: ignore
                        handicap -= 1
                    if handicap > 0:
                        komi = 0.5
        pygame.display.update()
        
main()