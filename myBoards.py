
###############################################################################

# Assignment 4: Tic Tac Toe Game
# Student Name: Hiba Kaawan
# Student ID: hkaawan
# Student Number: 250921401

###############################################################################

#Class Gameboard
class GameBoard:
    # creates a constructor to construct the board and creates instances variables to reference to the players
    def __init__(self, playerX, playerO):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.playerX = playerX
        self.playerO = playerO

#Method that prints current board
    def printCurrentBoard(self):
        print(self.board[0][0] + '|' + self.board[0][1] + '|' + self.board[0][2])
        print('-----')

        print(self.board[1][0] + '|' + self.board[1][1] + '|' + self.board[1][2])
        print('-----')

        print(self.board[2][0] + '|' + self.board[2][1] + '|' + self.board[2][2])

#Method that places X, and take 2 parameters, the row and column number
    def placeX(self,row, column):
        if row not in range(1, 4) or column not in range(1, 4):
            return False
        elif self.board[row-1][column-1] != ' ':
            return False
        else:
            if self.board[row-1][column-1] == ' ':
                self.board[row-1][column-1] = 'X'

#Method that places O, and takes 2 parameters, the row and column number
    def placeO(self, row, column):
        if row not in range(1, 4) or column not in range(1, 4):
            return False
        elif self.board[row-1][column-1] != ' ':
            return False
        else:
            if self.board[row-1][column-1] == ' ':
                self.board[row-1][column-1] = 'O'

#Method that decides winner, returns X or O if they win, returns none is no winner
    def decideWinner(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 'X':    #across the top
            winner = "X"
            return winner
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'X':  #across the middle
            winner = "X"
            return winner
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'X':  #across the bottom
            winner = "X"
            return winner
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'X':  #down left side
            winner = "X"
            return winner
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'X':  #down middle
            winner = "X"
            return winner
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'X':  #down the right side
            winner = "X"
            return winner
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X':  #diagonally from left to right
            winner = "X"
            return winner
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':  #diagonally from right to left
            winner = "X"

            return winner
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 'O':    #across the top
            winner = 'O'
            return winner
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'O':  #across the middle
            winner = 'O'
            return winner
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'O':  #across the bottom
            winner = 'O'
            return winner
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'O':  #down left side
            winner = 'O'
            return winner
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'O':  #down middle
            winner = 'O'
            return winner
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'O':  #down the right side
            winner = 'O'
            return winner
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':  #diagonally from left to right
            winner = 'O'
            return winner
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':  #diagonally from right to left
            winner = 'O'
            return winner
        else:
            return None
# Method that checks if the board is full or not
    def boardFull(self):
        if self.board[0][0] != ' ' and self.board[0][1] != ' ' and self.board[0][2] != ' ' and self.board[1][0] != ' ' and self.board[1][1] != ' ' and self.board[1][2] != ' ' and self.board[2][0] != ' ' and self.board[2][1] != ' ' and self.board[2][2] != ' ':
            return True
        else:
            return False

#class Scoreboard...it inherits Gameboard
class ScoreBoard(GameBoard):

# creates a constructor to construct the board and creates instances variables to reference to the players
    def __init__(self, player1, player2):
        self.player1 = str(player1)
        self.player2 = str(player2)
        self.players = [player1,player2]
        self.board = [[0, 0, 0],
                      [0, 0, 0]]
#Method that adds wins and adds it to the board
    def addWin(self, player):
        # goes thru the list to add the values if a player won or not and adds new values to that
        for i in range(len(self.players)):
            if player == self.players[i]:
                self.board[i][0] = self.board[i][0] + 1

#Method that adds losses and adds it to the board
    def addLoss(self, player):
        # goes thru the list to add the values if a player loss or not and adds new values to that
        for i in range(len(self.players)):
            if player == self.players[i]:
                self.board[i][1] = self.board[i][1] + 1

#Method that adds draws and adds it to the board
    def addDraw(self, player1, player2):
        # goes thru the list to add the values if the player is at a draw or not and adds new values to that
        for i in range(len(self.players)):
            if player1 == self.players[i]:
                self.board[i][2] = self.board[i][2] + 1
        for i in range(len(self.players)):
            if player2 == self.players[i]:
                self.board[i][2] = self.board[i][2] + 1

#Method that adds a new player to the list and adds it to the scoreboard
    def addPlayer(self, player1, player2):
        Playr = False
        for i in range(len(self.players)):
            if player1 == self.players[i]:
                Playr = True
        if Playr == False:
            data = {"win": 0, "loss": 0, "draw": 0}
            self.players.append(player1)
            self.board.append([data["win"],data["loss"],data["draw"]])
        Playr = False
        for i in range(len(self.players)):
            if player2 == self.players[i]:
                Playr = True
        if Playr == False:
            data = {"win": 0, "loss": 0, "draw": 0}
            self.players.append(player2)
            self.board.append([data["win"], data["loss"], data["draw"]])

#Method that prints scoreboard neatly
    def printScoreBoard(self):
        print("           Name | Wins | Losses | Draws")
        print("------------------------------------------")
        for i in range(len(self.players)):
            # printing the score board using the ljust to add spaces to evenly match the names
            print(self.players[i].ljust(18),
                  "|   {}  |   {}    |  {}  ".format(self.board[i][0], self.board[i][1], self.board[i][2]))
            # using .format to print the scoreboard
