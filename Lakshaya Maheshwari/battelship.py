from random import randint

board1 = []
board2=[]
flag=True
p1=0
p2=0
for x in range(5):
    board1.append(["O"] * 5)
    board2.append(["O"] * 5)

def print_board(board1):
    for row1 in board1:
        print (" ".join(row1))



print ("Let's play Battleship!")
print ("player1")
print_board(board1)
print
print ("player2")
print_board(board2)

def random_row1(board):
    return randint(0, len(board) - 1)

def random_col1(board):
    return randint(0, len(board[0]) - 1)

def random_row2(board):
    return randint(0, len(board) - 1)

def random_col2(board):
    return randint(0, len(board[0]) - 1)

ship_row1 = random_row1(board1)
ship_col1 = random_col1(board1)

ship_row2 = random_row1(board2)
ship_col2 = random_col1(board2)


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
while flag:


     if p1==0:
          print ("Player 1 Turn")
          guess_row1 = int(input("Guess Row:"))
          guess_col1 = int(input("Guess Col:"))
          if guess_row1 == ship_row1 and guess_col1 == ship_col1:
             print ("Congratulations!Player1 You sunk Player2 battleship!")
             break
          else:
             if(guess_row1<0 or guess_row1>4)or(guess_col1<0 or guess_col1>4):
                  print ("Oops, that's not even in the ocean.")
             elif(board1[guess_row1][guess_col1] == "X"):
                print ("You guessed that one already.")
             else:
                print ("You missed my battleship!")


                board2[guess_row1][guess_col1] = "X"
                print("Player2 Ship After Guess")
                print_board(board2)
    # Print (turn + 1) here!

          p1=1

     else:
         print ("Player 2 Turn")
         guess_row2 = int(input("Guess Row:"))
         guess_col2 = int(input("Guess Col:"))
         if guess_row2 == ship_row1 and guess_col2 == ship_col1:
             print ("Congratulations!Player2 You sunk Player1 battleship!")
             break
         else:
             if(guess_row2<0 or guess_row2>4)or(guess_col2<0 or guess_col2>4):
                  print ("Oops, that's not even in the ocean.")
             elif(board1[guess_row2][guess_col2] == "X"):
                print ("You guessed that one already.")
             else:
                print ("You missed my battleship!")


                board1[guess_row2][guess_col2] = "X"
                print("Player1 Ship After Guess")
                print_board(board1)
    # Print (turn + 1) here!

         p1=0









