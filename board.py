board = [
            ["-","-","-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
            ]

user = True

def printBoard(board):
    print("Printing board...")
    for i in range (3):
        print (board[i])
        
def quit(userInput1, userInput2):
    if (userInput1=="q" or userInput2=="q"):
        return False
    else:
        return True

def printSentence(currentPlayer): # Prompt player to input
    if user:
        print("Player 1, make your move")
    else: 
        print("Player 2, make your move")

def checkBoard(userInput1, userInput2, board): # Check if position on the board is in use
    row = int(userInput1)
    col = int(userInput2)
    if (board[row][col]!="-"):
        return True
    else:
        return False

def markBoard(userInput1, userInput2, board, currentPlayer): # Put mark on board
    row = int(userInput1)
    col = int(userInput2)
    board[row][col] = activePlayer

def currentPlayer(user): # Return different symbols to print on board
    if user:
        return "X"
    else:
        return "O"

def checkRow(user, board):
    for i in range (len(board)):
        if (board[0][i]==board[1][i] and board[1][i]==board[2][i]):
            return True
            break
        else:
            return False
            

def checkCol(user, board):
    for i in range (len(board)):
        if (board[i][0]==board[i][1] and board[i][1]==board[1][2])
            return True
            break
        else:
            return False

def checkDiag(user, board):
        if ((board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[2][0]==board[1][1] and board[1][1]==board[0][2]):
            return True
            break
        else:
            return False
            

def win(user, board):
    if checkRow(user, board):
        return True
    elif checkCol(user, board):
        return True
    elif checkDiag(user,board):
        return True
    else:
        print("It's a draw'")
        return False

def printWin(currentPlayer): # Prompt player to input
    if user:
        print("Player 1 won! Game over.")
    else: 
        print("Player 2 won! Game over.")
    

##def playerPosition(userInput1, userInput2):
##    row = int(userInput1)
##    col = int(userInput2)
##    return(row, col)
        
while True:
    activePlayer = currentPlayer(user)
    printBoard(board)
    
    userInput1 = input("Please enter row number (0-2): ")
    userInput2 = input("Please enter column number (0-2): ")
    
    if (userInput1!="0" and userInput1!="1" and userInput1!="2"):
        print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
        continue
    if (userInput2!="0" and userInput2!="1" and userInput2!="2"):
         print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
         continue
    
       
    checkBoard(userInput1, userInput2, board)
    if checkBoard(userInput1, userInput2, board):
        print("**** Board [" + row + "][" + col + "] has already been selected. Please select somewhere else on the board ****")
        print("**** Invalid choice. Please mark again! ****")
        continue
    markBoard(userInput1, userInput2, board, currentPlayer)
    if win(activePlayer, board):
        printWin(currentPlayer)
    user = not user
    