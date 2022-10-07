import pygame
from constants import BLACK, SQUARE_SIZE, DARK_GREY, DARK_WHITE
from stones import Stone
import copy
import os

class Board:
    def __init__(self):
        # Store board state
        self.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 'b', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 0, 1],
            [1, 'b', 'w', 'w', 'w', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 0, 1],
            [1, 0, 'w', 0, 0, 'w', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 1],
            [1, 0, 'w', 0, 0, 'w', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 'w', 'w', 'w', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 0, 'w', 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 'w', 'w', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 1],
            [1, 0, 'w', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b', 0, 1],
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
        self.black_territory = 'bt'
        self.white_territory = 'wt'
        self.neutral_territory = 'n'
        self.marker = 'x'
        self.liberty = '+'
        self.liberties = []
        self.white_to_move = False
        self.capture_board = True
        self.ko_board = None
        self.capture_count = 0
        self.ko_list_counter = -1
        self.ko_list = []
        self.board_img = pygame.image.load(os.path.join('images', 'Board1.png'))
        self.pass_count = 0
        self.score_border_b = False
        self.score_border_w = False
        self.territory_count = 0
        self.black_territory_count = 0
        self.white_territory_count = 0
        self.captued_white_stones = 0
        self.captued_black_stones = 0
        self.black_score = 0
        self.white_score = 6.5
        self.start_time = None

    def draw_board(self, win):
        self.draw_squares(win)
        self.draw_stones(win)

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
        for x in range(20):
            for y in range(20):
                stone = self.board[x][y]
                if stone == self.white_stone:
                    stone = Stone(x, y, DARK_WHITE)
                    stone.draw(win)
                elif stone == self.black_stone:
                    stone = Stone(x, y, BLACK)
                    stone.draw(win)

    def place_stone(self, row, col, placed_stone, opponent_stone):
        if self.capture_board == True:
            # Board capture prior player's turn
            self.ko_board = copy.deepcopy(self.board)
            # Avoid clicking on already placed stones
        if self.board[row][col] != placed_stone and self.board[row][col] != opponent_stone:
            self.board[row][col] = placed_stone
            # Switch turn
            self.white_to_move = not self.white_to_move
            self.check_move(row, col, placed_stone, opponent_stone)

    def pass_move(self):
        # Skip move if pass
        self.white_to_move = not self.white_to_move
        self.pass_count += 1
        # End game if pass from both players
        if self.pass_count == 2:
            print('Game end!')
            self.calc_score()
            self.print_board(self.board)
            print('White territory: ', self.white_territory_count)
            print('Black territory: ', self.black_territory_count)

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
                        self.capture_stones(opponent_stone)
                    self.restore_board(opponent_stone)
        # Check if move is suicidial
        if self.suicidal_move(row, col, placed_stone) == True:
            # If move is suicidal, keep the turn for the current player
            self.white_to_move = not self.white_to_move
            # If move is suicidal, do not capture board state
            self.capture_board = False
            # Set delay for invalid move message
            self.start_time = pygame.time.get_ticks()
        # Append board state if stone is captured in a ko state
        if self.capture_count >= 1 and self.stone_captured == True:
            self.ko_board2 = copy.deepcopy(self.board)
            self.ko_list.append(self.ko_board2)
            self.ko_list_counter += 1
        # Reset ko board list and counter if stone with liberties is placed on the board / Ko sequence is terminated
        if self.capture_board == True:
            self.capture_count = 0
            self.ko_list_counter = -1
            self.ko_list = []
            # Reset pass counter as a stone is placed
            self.pass_count = 0

    def calc_liberties(self, row, col, stone_to_calc):
        stone = self.board[row][col]
        if stone == stone_to_calc and self.board[row][col] != self.marker:
            # Save stone coordinates in the capture block board
            self.capture_block[row][col] = stone
            # Mark the stone
            self.board[row][col] = self.marker
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
            self.board[row][col] = self.liberty
            # Save the liberties in a list
            self.liberties.append(self.board[row][col])

    def capture_stones(self, stone_to_calc):
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
        if self.capture_count >= 2:
            self.ko = self.ko_list[self.ko_list_counter - 1]
        else:
            self.ko = self.ko_board
        # If it's a Ko move, restore the stone
        if self.ko == self.board:
            for x in range(21):
                for y in range(21):
                    stone = self.capture_block[x][y]
                    if self.capture_block[x][y] != 1 and stone == stone_to_calc:
                        # Restore the stone on the board if its a invalid Ko move
                        self.board[x][y] = stone_to_calc
                        # Restore captured stones count for the interface
                        if stone_to_calc == self.white_stone:
                            self.captued_white_stones -= 1
                        else:
                            self.captued_black_stones -= 1
                        # Set delay for invalid move message
                        self.start_time = pygame.time.get_ticks()
        else:
            # Stone is caputred
            self.stone_captured = True
            # Increase capture count for Ko calculations
            self.capture_count += 1
            # Reset pass counter
            self.pass_count = 0
        # Prevent capturing of the board
        self.capture_board = False

    def suicidal_move(self, row, col, stone_to_calc):
        self.calc_liberties(row, col, stone_to_calc)
        if len(self.liberties) == 0:
            # Set intersection as empty on the board if move is suicidial
            self.board[row][col] = 0
            # self.restore_board(stone_to_calc)
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
                    elif self.score_border_b == False and self.score_border_w == True:
                        self.white_territory_count += self.territory_count

                    self.score_border_b = False
                    self.score_border_w = False
                    self.territory_count = 0

    def calc_score_liberties(self, row, col):
        if self.board[row][col] != 0:
            if self.board[row][col] == self.black_stone:
                self.score_border_b = True
            elif self.board[row][col] == self.white_stone:
                self.score_border_w = True
            return

        self.board[row][col] = self.marker
        self.territory_count += 1
        # Walk North recursively
        self.calc_score_liberties(row - 1, col)
        # Walk East recursively
        self.calc_score_liberties(row, col + 1)
        # Walk South recursively
        self.calc_score_liberties(row + 1, col)
        # Walk West recursively
        self.calc_score_liberties(row, col - 1)

    def remove_dead_stones(self, row, col):
        pass

    # For debug
    def print_board(self, board):
        print('\nBoard:\n')
        for row in board:
            print(*row, sep=' ')