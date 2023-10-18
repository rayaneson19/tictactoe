#tictactoe
import os
os.system('cls')
the_board = {
    1 :' ',
    2 :' ',
    3 :' ',
    4 :' ',
    5 :' ',
    6 :' ',
    7 :' ',
    8 :' ',
    9 :' ',
            }
def xo(board):
    print(' _________________')
    print('|     |     |     |')
    print('|  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+'  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+'  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+'  |')
    print('|     |     |     |')
    print(' ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ')

c1 = True
c2 = False
c= True 
v_n = [1,2,3,4,5,6,7,8,9]
turns = 1
print(xo(the_board))
try:
    while c:
        while c1:
            n = int(input(' \n    Player X:   '))
            os.system('cls')
            if turns==9:
                print('Its a draw. ')
                c = False
                c1 = False
                c2 = False
                break
            if n not in v_n:
                print(' \n You can only type numbers from 1 to 9. \n ')
                break
            if the_board[n] == ' ':
                the_board[n] = 'X'
                xo(the_board)
                c1 = False
                c2 = True
                turns +=1
            else:
                print(" \n Position already occupied. Try again. \n ")
            if the_board[(1)] == the_board[(2)] == the_board[(3)] == 'X' or the_board[(1)] == the_board[(4)] == the_board[(7)] == 'X' or the_board[(7)] == the_board[(8)] == the_board[(9)] == 'X' or the_board[(9)] == the_board[(6)] == the_board[(3)] == 'X' or the_board[(8)] == the_board[(5)] == the_board[(2)] == 'X' or the_board[(4)] == the_board[(5)] == the_board[(6)] == 'X' or the_board[(1)] == the_board[(5)] == the_board[(9)] == 'X' or the_board[(7)] == the_board[(5)] == the_board[(3)] == 'X':
                print('Player O lost.')
                c = False
                c1 = False
                c2 = False
                break
        while c2:
            n = int(input(' \n    Player O:   '))
            os.system('cls')
            if turns==9:
                print('Its a draw. ')
                c = False
                c1 = False
                c2 = False
                break
            if n not in v_n:
                print(' \n You can only type numbers from 1 to 9. \n ')
                break
            if the_board[n] == ' ':
                the_board[n] = 'O'
                xo(the_board)
                c1 = True
                c2 = False
                turns +=1
            else:
                print(" \n Position already occupied. Try again. \n ")
            if the_board[(1)] == the_board[(2)] == the_board[(3)] == 'O' or the_board[(1)] == the_board[(4)] == the_board[(7)] == 'O' or the_board[(7)] == the_board[(8)] == the_board[(9)] == 'O' or the_board[(9)] == the_board[(6)] == the_board[(3)] == 'O' or the_board[(8)] == the_board[(5)] == the_board[(2)] == 'O' or the_board[(4)] == the_board[(5)] == the_board[(6)] == 'O' or the_board[(1)] == the_board[(5)] == the_board[(9)] == 'O' or the_board[(7)] == the_board[(5)] == the_board[(3)] == 'O':
                print('Player X lost.')
                c = False
                c1 = False
                c2 = False
                break
except ValueError:
    print(' \n You can only type numbers from 1 to 9. \n ')