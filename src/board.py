import pygame
from constants import BLACK, SQUARE_SIZE, DARK_GREY, DARK_WHITE, WHITE, WIN
from stones import Stone
import copy
import os

class Board:
    def __init__(self):
        # Store board state
        self.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        # Temporally store of stones\group of stones in a separate board for potential capturing
        self.capture_block = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.black_stone = 'b'
        self.white_stone = 'w'
        self.b_death_stone = 'bd'
        self.w_death_stone = 'wd'
        self.black_territory = 'bt'
        self.white_territory = 'wt'
        self.neutral_territory = 'n'
        self.stone_placed = False
        self.marker = 'x'
        self.liberty = '+'
        self.liberties = []
        self.white_to_move = False
        self.capture_board = True
        self.ko_board = None
        self.capture_count = 0
        self.ko_list_counter = -1
        self.ko_list = []
        self.board_img = pygame.image.load(os.path.join('src/images', 'board.png'))
        self.stone_sound = pygame.mixer.Sound(os.path.join('src/sounds', 'place.wav'))
        self.capture_sound = pygame.mixer.Sound(os.path.join('src/sounds', 'capture_single.wav'))
        self.capture_sound_m = pygame.mixer.Sound(os.path.join('src/sounds', 'capture_many.wav'))
        self.pass_sound = pygame.mixer.Sound(os.path.join('src/sounds', 'pass.wav'))
        self.remove_sound = pygame.mixer.Sound(os.path.join('src/sounds', 'remove.wav'))
        self.remove_sound_check = True
        self.pass_count = 0
        self.score_border_b = False
        self.score_border_w = False
        self.territory_count = 0
        self.black_territory_count = 0
        self.white_territory_count = 0
        self.captued_white_stones = 0
        self.captued_black_stones = 0
        self.captured_turn = 0
        self.komi = 6.5
        self.start_time = None
        self.game_end = False

    def draw_squares(self, win):
        win.fill(DARK_GREY)
        win.blit(self.board_img, (0, 0))
        for x in range(18):
            for y in range(18):
                pygame.draw.rect(win, BLACK, (x * SQUARE_SIZE + 23, y *
                                 SQUARE_SIZE + 23, SQUARE_SIZE + 2, SQUARE_SIZE + 2), 2)
        # Draw the dots
        pygame.draw.circle(win, BLACK, (144, 144), 5)
        pygame.draw.circle(win, BLACK, (144, 624), 5)
        pygame.draw.circle(win, BLACK, (624, 144), 5)
        pygame.draw.circle(win, BLACK, (624, 624), 5)
        pygame.draw.circle(win, BLACK, (144, 384), 5)
        pygame.draw.circle(win, BLACK, (624, 384), 5)
        pygame.draw.circle(win, BLACK, (384, 144), 5)
        pygame.draw.circle(win, BLACK, (384, 624), 5)
        pygame.draw.circle(win, BLACK, (384, 384), 5)

    def draw_stones(self, win):
        for x in range(21):
            for y in range(21):
                field = self.board[x][y]
                if field == self.white_stone:
                    field = Stone(x, y, DARK_WHITE)
                    field.draw_stone(win)
                elif field == self.black_stone:
                    field = Stone(x, y, BLACK)
                    field.draw_stone(win)
                elif field == self.black_territory:
                    field = Stone(x, y, BLACK)
                    field.draw_territory(win)
                elif field == self.white_territory:
                    field = Stone(x, y, WHITE)
                    field.draw_territory(win)
                elif field == self.w_death_stone:
                    field = Stone(x, y, WHITE)
                    field.draw_stone(win)
                    field.draw_cross(win)
                elif field == self.b_death_stone:
                    field = Stone(x, y, BLACK)
                    field.draw_stone(win)
                    field.draw_cross(win)

    def place_stone(self, row, col, placed_stone, opponent_stone):
        if self.capture_board == True:
            # Board capture prior player's turn
            self.ko_board = copy.deepcopy(self.board)
        if self.board[row][col] != placed_stone and self.board[row][col] != opponent_stone:
            self.board[row][col] = placed_stone
            self.white_to_move = not self.white_to_move
            self.check_move(row, col, placed_stone, opponent_stone)

    def pass_move(self):
        # Skip move if pass
        self.pass_sound.play()
        self.white_to_move = not self.white_to_move
        self.pass_count += 1
        if self.pass_count == 2:
            self.white_to_move = False

    def check_move(self, row, col, placed_stone, opponent_stone):
        self.capture_board = True
        self.stone_captured = False
        for x in range(21):
            for y in range(21):
                stone = self.board[x][y]
                if self.board[x][y] != 1 and stone == opponent_stone:
                    # Calculate opponent stones liberties
                    self.calc_liberties(x, y, opponent_stone)
                    if len(self.liberties) == 0:
                        # Try to capture opponent stone/s
                        self.capture_stones(opponent_stone, row, col)
                    self.restore_board(opponent_stone)
        # Check if move is suicidial
        if self.suicidal_move(row, col, placed_stone) == True:
            self.white_to_move = not self.white_to_move
            self.capture_board = False
            self.start_time = pygame.time.get_ticks()
        # Append board state if stone is captured in a ko state
        if self.capture_count >= 1 and self.stone_captured == True:
            self.ko_board2 = copy.deepcopy(self.board)
            self.ko_list.append(self.ko_board2)
            self.ko_list_counter += 1
        # Reset ko board list and counter if stone is placed on the board
        if self.capture_board == True:
            self.stone_sound.play()
            self.capture_count = 0
            self.ko_list_counter = -1
            self.ko_list = []
            self.pass_count = 0
            self.stone_placed = True
            self.pos_x = row
            self.pos_y = col

    def calc_liberties(self, row, col, stone_to_calc):
        stone = self.board[row][col]
        if stone == stone_to_calc and self.board[row][col] != self.marker:
            # Save stone coordinates in the capture block board
            self.capture_block[row][col] = stone
            # Mark the stone
            self.board[row][col] = self.marker  # type: ignore
            # Look for neighbors:
            # Walk North recursively
            self.calc_liberties(row - 1, col, stone_to_calc)
            # Walk East recursively
            self.calc_liberties(row, col + 1, stone_to_calc)
            # Walk South recursively
            self.calc_liberties(row + 1, col, stone_to_calc)
            # Walk West recursively
            self.calc_liberties(row, col - 1, stone_to_calc)
        # If the intersection is empty
        elif stone == 0:
            # Mark intersection as liberty
            self.board[row][col] = self.liberty  # type: ignore
            # Save the liberties in a list
            self.liberties.append(self.board[row][col])

    def capture_stones(self, stone_to_calc, row, col):
        # Set capture block for ko calculation
        for x in range(21):
            for y in range(21):
                stone = self.capture_block[x][y]
                if self.capture_block[x][y] != 1 and stone == stone_to_calc:
                    # Set intersection as empty on the board (capture)
                    self.board[x][y] = 0
                    # Increase captured stones count for the interface
                    if stone_to_calc == self.white_stone:
                        self.captued_white_stones += 1
                    else:
                        self.captued_black_stones += 1
                    self.captured_turn += 1
        if self.capture_count >= 2 and self.ko_list:
                self.ko = self.ko_list[self.ko_list_counter - 1]
        else:
            self.ko = self.ko_board
        pass
        # If it's a Ko move, restore the stone
        if self.ko == self.board:
            for x in range(21):
                for y in range(21):
                    stone = self.capture_block[x][y]
                    if self.capture_block[x][y] != 1 and stone == stone_to_calc:
                        self.board[x][y] = stone_to_calc
                        if stone_to_calc == self.white_stone:
                            self.captued_white_stones -= 1
                        else:
                            self.captued_black_stones -= 1
                        self.captured_turn -= 1
                        # Set delay for invalid move message
                        self.start_time = pygame.time.get_ticks()
        else:
            self.stone_captured = True
            # Increase capture count for Ko calculations
            self.capture_count += 1
            # Reset pass counter
            self.pass_count = 0
            # Play capture sound
            if self.captured_turn == 1:
                self.capture_sound.play()
            else:
                self.capture_sound_m.play()
            self.captured_turn = 0
            self.pos_x = row
            self.pos_y = col
        # Prevent capturing of the board
        self.capture_board = False

    def suicidal_move(self, row, col, stone_to_calc):
        self.calc_liberties(row, col, stone_to_calc)
        if len(self.liberties) == 0:
            # Set intersection as empty on the board if move is suicidial
            self.board[row][col] = 0
            self.restore_board(stone_to_calc)
            return True
        self.restore_board(stone_to_calc)

    def restore_board(self, stone_to_calc):
        # Clear capture block board
        for x in range(21):
            for y in range(21):
                if self.capture_block[x][y] != 1:
                    self.capture_block[x][y] = 0
        # Clear liberties list
        self.liberties = []
        # Unmark placed stones on the board
        for x in range(21):
            for y in range(21):
                if self.board[x][y] != 1 and self.board[x][y] == self.marker:
                    self.board[x][y] = stone_to_calc
        # Unmark liberties on the board
        for x in range(21):
            for y in range(21):
                if self.board[x][y] != 1 and self.board[x][y] == self.liberty:
                    self.board[x][y] = 0

    def calc_score(self):
        for x in range(21):
            for y in range(21):
                if self.board[x][y] != self.marker and self.board[x][y] == 0:
                    self.calc_score_liberties(x, y)
                    if self.score_border_b == True and self.score_border_w == False:
                        self.black_territory_count += self.territory_count
                        for a in range(21):
                            for b in range(21):
                                if self.board[a][b] == self.marker:
                                    self.board[a][b] = self.black_territory  # type: ignore
                    elif self.score_border_b == False and self.score_border_w == True:
                        self.white_territory_count += self.territory_count
                        for a in range(21):
                            for b in range(21):
                                if self.board[a][b] == self.marker:
                                    self.board[a][b] = self.white_territory  # type: ignore
                    else:
                        for a in range(21):
                            for b in range(21):
                                if self.board[a][b] == self.marker:
                                    self.board[a][b] = self.neutral_territory  # type: ignore
                    self.score_border_b = False
                    self.score_border_w = False
                    self.territory_count = 0
        self.game_end = True

    def calc_score_liberties(self, row, col):
        if self.board[row][col] != 0 and self.board[row][col] != 'bd' and self.board[row][col] != 'wd':
            if self.board[row][col] == self.black_stone:
                self.score_border_b = True
            elif self.board[row][col] == self.white_stone:
                self.score_border_w = True
            return

        self.board[row][col] = self.marker  # type: ignore
        self.territory_count += 1
        # Walk North recursively
        self.calc_score_liberties(row - 1, col)
        # Walk East recursively
        self.calc_score_liberties(row, col + 1)
        # Walk South recursively
        self.calc_score_liberties(row + 1, col)
        # Walk West recursively
        self.calc_score_liberties(row, col - 1)

    def remove_dead_stones(self, row, col, turn):
        # Dead black stones
        if turn == False and self.board[row][col] == self.black_stone:
            self.board[row][col] = self.b_death_stone  # type: ignore
            self.captued_black_stones += 1
        elif turn == False and self.board[row][col] == self.b_death_stone:
            self.board[row][col] = self.black_stone  # type: ignore
            self.captued_black_stones -= 1
        # Dead white stones
        elif turn == True and self.board[row][col] == self.white_stone:
            self.board[row][col] = self.w_death_stone  # type: ignore
            self.captued_white_stones += 1
        elif turn == True and self.board[row][col] == self.w_death_stone:
            self.board[row][col] = self.white_stone  # type: ignore
            self.captued_white_stones -= 1

    def draw_circle(self, win, row, col, turn):
            x = SQUARE_SIZE * (col) + SQUARE_SIZE // 2
            y = SQUARE_SIZE * (row) + SQUARE_SIZE // 2
            if turn == False:
                pygame.draw.circle(win, BLACK, (x - 36, y - 36), 12, width = 3)
            else:
                pygame.draw.circle(win, WHITE, (x - 36, y - 36), 12, width = 3)

    # For debug
    def print_board(self, board):
        print('\nBoard:\n')
        for row in board:
            print(*row, sep=' ')