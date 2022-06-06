
###############################################################################

# Assignment 4: Tic Tac Toe Game
# Student Name: Hiba Kaawan
# Student ID: hkaawan
# Student Number: 250921401

###############################################################################
#Importing classes frrom myBoards.py
from myBoards import *

#Printing instuctions, and prompting user for names, and setting their name to either "x" or "o"
print("We are playing tic tac toe!")
print("To play the game enter two numbers to indicate where to place")
print("each game piece.  Enter numbers from 1 to 3.")
print("(1,1) is the top left corner.  (3,3) is the bottom right corner.")
playerX = str(input("Who is playing as X? "))
playerO = str(input("Who is playing as O? "))
scoreBoard = ScoreBoard(playerX, playerO)

#Main function that takes 2 parameters, player x and player o
def main(playerX,playerO):
    board = GameBoard(playerX, playerO)
    board.printCurrentBoard()
    outcome = False
    while outcome == False:
        print("Its", playerX + "'s", "turn!")
        while True:
            try:
                moveX = str(input("Where should X go?"))    #prompting user for x placement
                moveSplit = moveX.split()                 #splits their input
                print(moveSplit)
                row = int(moveSplit[0])
                column = int(moveSplit[1])
                if board.placeX(row, column) != False:      #uses the placex method...if it returns true, it breaks out of the loop
                    break
                if board.placeX(row, column) == False:      #uses the placex method...if it returns false, and prints an invalid statement
                    print("Sorry, invalid input.\nPlease try again.")

            except:
                print("Sorry, invalid input.\nPlease try again.")

#This controls playerX
        if board.decideWinner() == "X" or board.decideWinner() == "O":
            print("Winner is", board.decideWinner() + "!")        #decide if win
            board.printCurrentBoard()                       #prints board
            scoreBoard.addWin(playerX)                      #adds a win to player x
            scoreBoard.addLoss(playerO)                     #adds a loss to player o
            scoreBoard.printScoreBoard()                    #prints the scoreboard
            break


        if board.boardFull() == True:           #determines if draw using the boardFull() method
            print("That game ended in a draw!")
            board.printCurrentBoard()
            scoreBoard.addDraw(playerX, playerO)
            scoreBoard.printScoreBoard()
            break
        board.printCurrentBoard()


        print("Its", playerO + "'s", "Turn!")
        while True:
            try:
                moveO = str(input("Where should O go?"))    #prompting user for O placement
                moveSplit = moveO.split()                   #splits their input
                row = int(moveSplit[0])
                column = int(moveSplit[1])
                if board.placeO(row, column) != False:      #uses the placeO method...if it returns true, it breaks out of the loop
                    break

                if board.placeO(row, column) == False:      #uses the placeO method...if it returns false, and prints an invalid statement
                    print("Sorry, invalid input.\nPlease try again.")
            except:
                print("Sorry, invalid input.\nPlease try again.")

#This controls playerO
        if board.decideWinner() == "X" or board.decideWinner() == "O":
            print("Winner is", board.decideWinner() + "!")                    #decide if win
            board.printCurrentBoard()                                   #prints board
            scoreBoard.addWin(playerO)                                  #adds a win to player o
            scoreBoard.addLoss(playerX)                                 #adds a win to player x
            scoreBoard.printScoreBoard()                                #prints scoreboard
            break

        if board.boardFull() == True:                       #determines if draw using the the boardFull method
            print("That game ended in a draw!")
            board.printCurrentBoard()
            scoreBoard.addDraw(playerX,playerO)
            scoreBoard.printScoreBoard()
            break

        board.printCurrentBoard()                           #prints the current board

#determing if they want to play again
main(playerX,playerO)
playAgain = str(input("Do You Want To Play Again? (Y/N)")).upper()
#if yes enters a while loop where main function is called again
while 'Y' in playAgain.upper():
    playerX = str(input("Who is playing as X? "))
    playerO = str(input("Who is playing as O? "))
    scoreBoard.addPlayer(playerX,playerO)
    main(playerX,playerO)
    playAgain = str(input("Do You Want To Play Again? (Y/N)")).upper()






