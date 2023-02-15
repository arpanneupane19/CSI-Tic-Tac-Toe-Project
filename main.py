# Computer Science I (Lawrence E. Elkins HS)
# Code written by Arpan Neupane from February 10, 2023 - February 16, 2023.
# Copyright (c) 2023 Arpan Neupane. All rights reserved.

import random


class TicTacToe:

    # Global class variables (self.var_name is used to reference)
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    current_player = random.choice(['X', 'O'])
    game_over = False
    winner = None

    # Changing turns logic
    def change_turn(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    # class method to display board
    # filters through the 2D array and prints each inner array
    def display_board(self):
        print('\n')
        for row in self.board:
            print(row)
        print('\n')

    # This will check if a spot is already occupied, invalid, etc.
    def check_valid_spot(self, spot):
        if (1 <= spot <= 9):
            if (1 <= spot <= 3):
                if (self.board[0][spot-1]) == '_':
                    return True
                else:
                    print("\nCannot put piece there.\n")
                    return False

            elif (4 <= spot <= 6):
                if (self.board[1][spot-4]) == '_':
                    return True
                else:
                    print("\nCannot put piece there.\n")
                    return False

            elif (7 <= spot <= 9):
                if (self.board[2][spot-7]) == '_':
                    return True
                else:
                    print("\nCannot put piece there.\n")
                    return False
        else:
            print("\nCannot put piece there.\n")
            return False

    def place_piece(self, spot):
        # filling up certain spots on the board by setting them equal to the current player
        if 1 <= spot <= 3:
            self.board[0][spot - 1] = self.current_player
        elif 4 <= spot <= 6:
            self.board[1][spot - 4] = self.current_player
        elif 7 <= spot <= 9:
            self.board[2][spot - 7] = self.current_player

    # function used to check for the winner
    # runs after every move to check winner
    # winner is mentioned via print() with a description on how they won (rows, columns, diagonals)
    def check_winner(self):
        # row checking
        for row in self.board:
            if row[0] == "X" and row[1] == "X" and row[2] == "X":
                self.winner = "X"
                print("\n{}'s wins via row!".format(self.winner))
                self.game_over = True

            elif row[0] == "O" and row[1] == "O" and row[2] == "O":
                self.winner = "O"
                print("\n{}'s wins via row!".format(self.winner))
                self.game_over = True

        # column checking
        if (self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X") or (self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X") or (self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X"):
            self.winner = "X"
            print("\n{}'s wins via column!".format(self.winner))
            self.game_over = True

        elif (self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[2][0] == "O") or (self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[2][1] == "O") or (self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[2][2] == "O"):
            self.winner = "O"
            print("\n{}'s wins via column!".format(self.winner))
            self.game_over = True

        # diagonal checking
        if (self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X") or (self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X"):
            self.winner = "X"
            print("\n{}'s wins via diagonal!".format(self.winner))
            self.game_over = True

        elif (self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O") or (self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O"):
            self.winner = "O"
            print("\n{}'s wins via diagonal!".format(self.winner))
            self.game_over = True

        # if there is a winner (X or O), the winning board is displayed and returns the number of moves that it took for the player to win.
        if self.winner == "X":
            moves = 0
            for row in self.board:
                moves += row.count("X")
            self.display_board()
            print("{} won in {} moves.".format(self.current_player, moves))

        elif self.winner == "O":
            moves = 0
            for row in self.board:
                moves += row.count("O")
            self.display_board()
            print("{} won in {} moves.".format(self.current_player, moves))

    # if there are no winners, check for a draw by checking if the board is filled up
    def check_draw(self):
        if self.winner is None:
            if (self.board[0][0] != "_" and self.board[0][1] != '_' and self.board[0][2] != '_') and (self.board[1][0] != '_' and self.board[1][1] != '_' and self.board[1][2] != '_') and (self.board[2][0] != '_' and self.board[2][1] != '_' and self.board[2][2] != '_'):
                self.winner = "Draw!".upper()
                self.display_board()
                print('\n{}\n'.format(self.winner))
                self.game_over = True

    # main play function that loops over and over until game is over (see conditional at end of file)
    def play(self):

        # display board and introduce the game to the players
        self.display_board()
        print(self.current_player + "'s" + " turn \n")
        spot = int(input("Pick a spot through 1-9: "))

        # check for the validity of the spot
        # if the spot is taken or invalid, the check_valid_spot(arg) method will return false
        valid_spot = self.check_valid_spot(spot)

        while not valid_spot:
            spot = int(input("Pick a spot through 1-9: "))
            valid_spot = self.check_valid_spot(spot)

        if valid_spot:
            self.place_piece(spot)
            self.check_winner()
            self.check_draw()
            self.change_turn()


# using this conditional so that the code under this is only executable in this file only.
if __name__ == "__main__":
    game = TicTacToe()
    while not game.game_over:
        game.play()
