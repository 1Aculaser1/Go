import pygame
import sys
from constants import SQUARE_SIZE, FPS, WIN, DARK_WHITE, BLACK, WHITE, DARK_GREY, LIGHT_GREY, RED, GREEN
from board import Board
from interface import Button, Text, remove_sound, black_wins_sound, white_wins_sound, logo, main_logo, title_text
from stones import Stone

new_game = False
pygame.display.set_caption(title_text)
pygame.display.set_icon(logo)

# Transform mouse position into rows and columns of the board list
def get_row_col_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    global new_game
    run = True
    play_win_sound = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # In-Game Events
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and new_game == True:
                # If stone is placed on the board
                if 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count < 2:
                    row, col = get_row_col_mouse(pos)
                    if board.white_to_move == False:
                        placed_stone = board.black_stone
                        opponent_stone = board.white_stone
                    else:
                        placed_stone = board.white_stone
                        opponent_stone = board.black_stone
                    board.place_stone(row + 1, col + 1, placed_stone, opponent_stone)
                # If pass button is clicekd
                if (
                    796 <= pos[0] <= 796 + 70 and 100 <= pos[1] <= 100 + 40
                    and board.pass_count < 2
                    and board.white_to_move == False
                ):
                    board.pass_move()
                if (
                    796 <= pos[0] <= 796 + 70 and 427 <= pos[1] <= 427 + 40
                    and board.pass_count < 2
                    and board.white_to_move == True
                ):
                    board.pass_move()
                # If game has ended, mark the death stones
                if ( 
                    12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 
                    and board.pass_count == 2
                ):
                    row, col = get_row_col_mouse(pos)
                    board.remove_dead_stones(row + 1, col + 1, board.white_to_move)
                # If ready button is clicked (black)
                if (
                    796 <= pos[0] <= 796 + 85 and 124 <= pos[1] <= 124 + 35
                    and board.pass_count == 2
                ):
                    board.white_to_move = True
                # If ready button is clicked (white)
                if (
                    796 <= pos[0] <= 796 + 85 and 454 <= pos[1] <= 454 + 35
                    and board.pass_count == 2
                ):
                    board.calc_score()
                # If new game button is clicked (during game)
                if 796 <= pos[0] <= 796 + 130 and 607 <= pos[1] <= 607 + 35:
                    main()
            # Pre-Game Events
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and new_game == False:
                # If new game button is clicked (before game)
                if 796 <= pos[0] <= 796 + 130 and 607 <= pos[1] <= 607 + 35:
                    new_game = True
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # If settings button is clicked
                if 796 <= pos[0] <= 796 + 130 and 693 <= pos[1] <= 693 + 35:
                    print('Options')
                # If exit game button is clicked
                if 796 <= pos[0] <= 796 + 144 and 650 <= pos[1] <= 650 + 35:
                    pygame.QUIT
                    sys.exit()

        if new_game == True:
            board.draw_squares(WIN)
            # Show the stone at mouse cursor
            if 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755 and board.pass_count < 2:
                row, col = get_row_col_mouse(pos)
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
                turn_b = Button(796, 23, 200, 65, LIGHT_GREY)
                if 796 <= pos[0] <= 796 + 70 and 100 <= pos[1] <= 100 + 40:
                    pass_b = Button(796, 100, 70, 40, LIGHT_GREY)
                else:
                    pass_b = Button(796, 100, 70, 40, DARK_GREY)
                pass_b_txt = Text(801, 105, 'pass', WHITE, 'font1')
            elif board.pass_count < 2 and board.white_to_move == True:
                turn_b = Button(796, 350, 200, 65, LIGHT_GREY)
                if 796 <= pos[0] <= 796 + 70 and 427 <= pos[1] <= 427 + 40:
                    pass_b = Button(796, 427, 70, 40, LIGHT_GREY)
                else:
                    pass_b = Button(796, 427, 70, 40, DARK_GREY)
                pass_b_txt = Text(801, 432, 'pass', WHITE, 'font1')
            # Draw pass button
            if board.start_time and pygame.time.get_ticks() - board.start_time < 600:
                inv_move_b = Button(282, 367, 201, 35, LIGHT_GREY)
                inv_move_txt = Text(287, 372, 'Invalid Move!', RED, 'font2')
            # Remove dead stones
            if board.pass_count == 2 and board.game_end == False:
                if board.remove_sound_check == True:
                    remove_sound.play()
                    board.remove_sound_check = False
                if board.white_to_move == False:
                    remove_b = Button(775, 20, 242, 92, LIGHT_GREY)
                    remove_txt = Text(780, 88, 'Remove the death stones', RED, 'font3')
                    if 796 <= pos[0] <= 796 + 85 and 124 <= pos[1] <= 124 + 35:
                        ready_b = Button(796, 124, 85, 35, LIGHT_GREY)
                    else:
                        ready_b = Button(796, 124, 85, 35, DARK_GREY)
                    ready_txt = Text(801, 129, 'Ready', WHITE, 'font1')
                else:
                    remove_b = Button(775, 350, 242, 92, LIGHT_GREY)
                    remove_txt = Text(780, 415, 'Remove the death stones', RED, 'font3')
                    if 796 <= pos[0] <= 796 + 85 and 454 <= pos[1] <= 454 + 35:
                        ready_b = Button(796, 454, 85, 35, LIGHT_GREY)
                    else:
                        ready_b = Button(796, 454, 85, 35, DARK_GREY)
                    ready_txt = Text(801, 459, 'Ready', WHITE, 'font1')
            # Draw players text
            black_player = Text(801, 28, 'Black', WHITE, 'font1')
            capture_count_b = Text(801, 63, 'Captured Stones: ' + str(board.captued_white_stones), WHITE, 'font3')
            white_player = Text(801, 355, 'White', WHITE, 'font1')
            capture_count_w = Text(801, 390, 'Captured Stones: ' + str(board.captued_black_stones), WHITE, 'font3')
            # Final score
            if board.game_end == True:
                black_territory_txt = Text(801, 88, 'Territory: ' + str(board.black_territory_count), WHITE, 'font3')
                black_total_score_txt = Text(801, 113, 'Total Score: ' + str(board.black_territory_count + board.captued_white_stones), WHITE, 'font4')
                white_territory_txt = Text(801, 415, 'Territory: ' + str(board.white_territory_count), WHITE, 'font3')
                komi_txt = Text(801, 439, f'Komi: {board.komi}', WHITE, 'font3')
                white_total_score_txt = Text(801, 464, 'Total Score: ' + str(board.white_territory_count + board.captued_black_stones + board.komi), WHITE, 'font4')
                if board.white_territory_count + board.captued_black_stones + board.komi > board.black_territory_count + board.captued_white_stones:
                    wins_txt = Text(801, 355, 'White Wins!', GREEN, 'font1')
                    if play_win_sound == True:
                        white_wins_sound.play()
                else:
                    wins_txt = Text(801, 28, 'Black Wins!', GREEN, 'font1')
                    if play_win_sound == True:
                        black_wins_sound.play()
                play_win_sound = False
        else:
            WIN.fill(DARK_GREY)
            WIN.blit(main_logo, (0, 0))
        # Draw New Game
        if 796 <= pos[0] <= 796 + 130 and 607 <= pos[1] <= 607 + 35:
            new_game_b = Button(796, 607, 130, 35, LIGHT_GREY)
        else:
            new_game_b = Button(796, 607, 130, 35, DARK_GREY)
        new_game_txt = Text(801, 612, 'New Game', WHITE, 'font2')
        # Draw Exit Game
        if 796 <= pos[0] <= 796 + 144 and 650 <= pos[1] <= 650 + 35:
            quit_b = Button(796, 650, 144, 35, LIGHT_GREY)
        else:
            quit_b = Button(796, 650, 144, 35, DARK_GREY)
        quit_txt = Text(801, 655, 'Exit Game', WHITE, 'font2')
        # Draw Options
        if 796 <= pos[0] <= 796 + 130 and 693 <= pos[1] <= 693 + 35:
            oprions_b = Button(796, 693, 130, 35, LIGHT_GREY)
        else:
            options_b = Button(796, 693, 130, 35, DARK_GREY)
        options_txt = Text(801, 698, 'Settings', WHITE, 'font2')
        pygame.display.update()
        
main()