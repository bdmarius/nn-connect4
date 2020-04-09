import copy

RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
GAME_STATE_NOT_ENDED = 2

class GameController:

    def __init__(self, game, redPlayer, yellowPlayer):
        self.game = game
        self.redPlayer = redPlayer
        self.yellowPlayer = yellowPlayer
        self.trainingHistory = []

    def simulateManyGames(self, numberOfGames):
        redPlayerWins = 0
        yellowPlayerWins = 0
        draws = 0
        for i in range(numberOfGames):
            self.game.resetBoard()
            self.playGame()
            if self.game.getGameResult() == RED_PLAYER_VAL:
                redPlayerWins = redPlayerWins + 1
            elif self.game.getGameResult() == YELLOW_PLAYER_VAL:
                yellowPlayerWins = yellowPlayerWins + 1
            else:
                draws = draws + 1
        totalWins = redPlayerWins + yellowPlayerWins + draws
        print('Red Wins: ' + str(int(redPlayerWins * 100 / totalWins)) + '%')
        print('Yellow Wins: ' + str(int(yellowPlayerWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')

    def playGame(self):
        playerToMove = self.redPlayer
        while self.game.getGameResult() == GAME_STATE_NOT_ENDED:
            availableMoves = self.game.getAvailableMoves()
            move = playerToMove.getMove(availableMoves, self.game.getBoard())
            self.game.move(move, playerToMove.getPlayer())
            if playerToMove == self.redPlayer:
                playerToMove = self.yellowPlayer
            else:
                playerToMove = self.redPlayer

        for historyItem in self.game.getBoardHistory():
            self.trainingHistory.append((self.game.getGameResult(), copy.deepcopy(historyItem)))


    def getTrainingHistory(self):
        return self.trainingHistory


