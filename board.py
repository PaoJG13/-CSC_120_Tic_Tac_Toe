class tictactoe:
    def printBoard():
        board = [
            ["-","-","-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
            ]
        print("Printing board...")
        for row in board:
            for slot in row:
                print(slot, end="")
            print()

    def userInput():
        row = input("Please enter row number (0-2): ")
        col = input("Please enter column number (0-2): ")
        if (row!=0 and row!=1 and row!=2):
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
            continue
        if (col!=0 and col!=1 and col!=2):
            print("**** Invalid row or column. Please select row / col between values 0 to 2 ****")
            continue

    def checkBoard(userInput):
        
        

printBoard()
while True:
    