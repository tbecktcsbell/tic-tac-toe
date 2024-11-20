def start_game():
  board=[
    ['#', '#', '#'],
    ['#', '#', '#'],
    ['#', '#', '#'],
  ] 
  
  show_board(board)
  
  for turn in range(9):
      print(turn)
      print(turn%2)
      show_board(board)
      place_piece(board, turn)
      winner = check_board(board)
      if(winner!="#"):
          print(f"Player {winner} won the game!!!")

  place_piece(board, 2)
def show_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col],end="")
        print("")

def place_piece(board, turn):
    pieces = ["X", "O"]
    piece = pieces[turn%2]

    row = int(input("Enter Row Index:"))
    col= int(input("Enter Col Index:"))

    while (board[row][col] != "#"):
        print("Please Pick An Empty Spot!")
        row = int(input("Enter Row Index:"))
        col= int(input("Enter Col Index:"))
    
    board[row][col] = piece
    show_board(board)

def check_board(board):

    for row in range(len(board)):
        if(board[row][0]!="#"):
            if(board[row][0]==board[row][1] and board[row][1]==board[row][2]):
                return board[row][0]
                

    for col in range(3):
        if(board[col][0]!="#"):
            if(board[col][0]==board[col][1] and board[col][1]==board[col][2]):
                return board[col][0]

    if(board[0][0]!="#"):
        if(board[0][0]==board[1][1] and board[1][1]==board[2][2]):
             return board[0][0]
            
    if(board[2][0]!="#"):
        if(board[2][0]==board[1][1] and board[1][1]==board[0][2]):
            return board[2][0]

start_game()