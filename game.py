import os
import copy

RED_PLAYER = 'R'
YELLOW_PLAYER = 'Y'
RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
EMPTY = ' '
EMPTY_VAL = 0
HORIZONTAL_SEPARATOR = ' | '
GAME_STATE_X = -1
GAME_STATE_O = 1
GAME_STATE_DRAW = 0
GAME_STATE_NOT_ENDED = 2
VERTICAL_SEPARATOR = '__'
NUM_ROWS = 6
NUM_COLUMNS = 7
REQUIRED_SEQUENCE = 4


class Game:

    def __init__(self):
        self.resetBoard()

    def resetBoard(self):
        self.board = [
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL]
        ]
        self.boardHistory = []

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print (VERTICAL_SEPARATOR, end='')
            print (os.linesep)
            for j in range(len(self.board[i])):
                if RED_PLAYER_VAL == self.board[i][j]:
                    print(RED_PLAYER, end='')
                elif YELLOW_PLAYER_VAL == self.board[i][j]:
                    print(YELLOW_PLAYER, end='')
                elif EMPTY_VAL == self.board[i][j]:
                    print(EMPTY, end='')
                print(HORIZONTAL_SEPARATOR, end='')
            print (os.linesep)
            for j in range(len(self.board[i])):
                print(VERTICAL_SEPARATOR, end='')
        print (os.linesep)

    def getAvailableMoves(self):
        availableMoves = []
        for j in range(NUM_COLUMNS):
            if self.board[NUM_ROWS - 1][j] == EMPTY_VAL:
                availableMoves.append([NUM_ROWS - 1, j])
            else:
                for i in range(NUM_ROWS - 1):
                    if self.board[i][j] == EMPTY_VAL and self.board[i + 1][j] != EMPTY_VAL:
                        availableMoves.append([i, j])
        return availableMoves

    def getGameResult(self):
        winnerFound = False
        currentWinner = None
        # Find winner on horizontal
        for i in range(NUM_ROWS):
            if not winnerFound:
                for j in range(NUM_COLUMNS - REQUIRED_SEQUENCE - 1):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j + 2] and \
                            self.board[i][j] == self.board[i][j + 3]:
                        currentWinner = self.board[i][j]
                        winnerFound = True

        # Find winner on vertical
        if not winnerFound:
            for j in range(NUM_COLUMNS):
                if not winnerFound:
                    for i in range(NUM_ROWS - REQUIRED_SEQUENCE - 1):
                        if self.board[i][j] != 0 and self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i+2][j] and \
                                self.board[i][j] == self.board[i+3][j]:
                            currentWinner = self.board[i][j]
                            winnerFound = True

        # Check lower left diagonals
        if not winnerFound:
            for i in range(NUM_ROWS - REQUIRED_SEQUENCE - 1):
               j = 0
               while j <= i:
                   if self.board[i][j] != 0 and self.board[i][i] == self.board[i + 1][j + 1] and self.board[i][i] == self.board[i + 2][j + 2] and \
                           self.board[i][i] == self.board[i + 3][j + 3]:
                       currentWinner = self.board[i][j]
                       winnerFound = True
                   j = j+1

        # Check upper right diagonals
        if not winnerFound:
            for j in range(NUM_COLUMNS - REQUIRED_SEQUENCE - 1):
                i = j
                while i<= NUM_ROWS - REQUIRED_SEQUENCE - 1:
                    if self.board[i][j] != 0 and self.board[i][i] == self.board[i + 1][j + 1] and self.board[i][i] == self.board[i + 2][j + 2] and \
                            self.board[i][i] == self.board[i + 3][j + 3]:
                        currentWinner = self.board[i][j]
                        winnerFound = True
                    i = i+1

        if winnerFound: return currentWinner
        else:
            drawFound = True
            # Check for draw
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == EMPTY_VAL:
                        drawFound = False
            if drawFound:
                return GAME_STATE_DRAW
            else:
                return GAME_STATE_NOT_ENDED

    def move(self, move, player):
        self.board[move[0]][move[1]] = player
        self.boardHistory.append(copy.deepcopy(self.board))

    def getBoardHistory(self):
        return self.boardHistory

    def getBoard(self):
        return self.board


