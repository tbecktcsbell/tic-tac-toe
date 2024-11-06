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

    board[row][col] = piece
    show_board(board)

def check_board(board):
    for row in board:
        for col in row:
            
start_game()

