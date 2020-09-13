tictactoe=[' ']*10
tictactoe[0]="#"

def playBoard():
   print(tictactoe[1]+' | '+tictactoe[2]+' | '+tictactoe[3])
   print("--------")
   print(tictactoe[4]+' | '+tictactoe[5]+' | '+tictactoe[6])
   print("--------")
   print(tictactoe[7]+' | '+tictactoe[8]+' | '+tictactoe[9])

def win(qwe):
   return ((tictactoe[1]==tictactoe[2]==tictactoe[3]==qwe)or(tictactoe[4]==tictactoe[5]==tictactoe[6]==qwe)or(tictactoe[7]==tictactoe[8]==tictactoe[9]==qwe)or(tictactoe[1]==tictactoe[5]==tictactoe[9]==qwe)or(tictactoe[3]==tictactoe[5]==tictactoe[7]==qwe)or(tictactoe[1]==tictactoe[4]==tictactoe[7]==qwe)or(tictactoe[2]==tictactoe[5]==tictactoe[8]==qwe)or(tictactoe[3]==tictactoe[6]==tictactoe[9]==qwe))

def isBlank(pos):
   return (tictactoe[pos]==' ')

def game():
   choose = input("choose 'X' or 'O'").upper()
   if (choose == 'X'):
      choose1 = 'O'
   else:
      choose1 = 'X'
   turn = 'first'
   while (1):
      if (' ' not in tictactoe):
         print("It's a draw :(")
         break
      elif (turn == 'first'):
         print("Player 1's turn")
         pos = int(input('Enter your position:'))
         print()
         if (isBlank(pos)):
            tictactoe[pos] = choose
            playBoard()
         else:
            print('Enter correct position')
         if (win(choose)):
            print("Player 1 wins!!!!!")
            print()
            break
         else:
            turn = 'second'
      elif (turn == 'second'):
         print("Player 2's turn")
         pos = int(input('Enter your position:'))
         print()
         if (isBlank(pos)):
            tictactoe[pos] = choose1
            playBoard()
         else:
            print('Enter correct position')
         if (win(choose1)):
            print("Player 2 wins!!!!!")
            print()
            break
         else:
            turn = 'first'

if __name__=='__main__':
    while(1):
        game()
        tictactoe=[' ']*10
        replay=input("Replay 'Y' or 'N'").upper()
        if(replay=='Y'):
            continue
        else:
            print('Thank you')
            break