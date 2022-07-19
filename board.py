firstRow = ["-", "-", "-"]
secondRow = ["-", "-", "-"]
thirdRow = ["-", "-", "-"]

print("\n");
print("Printing board...\n")

print(firstRow)
print(secondRow)
print(thirdRow)

def player1():
  print("Player 1, make your move\n")
  row = input("Enter row number (0-2): ")
  column = input("Enter column number (0-2): ")
  print("Player 1 added a mark at location " + row + ", " + column)
  

player1()
