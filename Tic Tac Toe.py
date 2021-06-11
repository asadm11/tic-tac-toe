import random

def display_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_marker():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    return p1,p2

def first_chance():
    return random.randint(1,3)

def place_marker(marker, pos):
    board[pos] = marker
    display_board(board)

def check_winner(marker):
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker) or
    (board[1] == board[5] == board[9] == marker))

def check_tie():
    for i in range(1,10):
        if space_check(i):
            return False
    return True

def space_check(pos):
    return board[pos] == ' ' 

def player_move(p):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(position):
        position = int(input('player ' + p + ': Enter your Position:  '))
    return position

def replay():
    return input('Do you want to play again? ').lower().startswith('y')

import time

print('\n\n\n\n\n\n\n\t\t\t Welcome to Tic-Tac-Toe :) :)')
time.sleep(2)
print('\n\n\t\t\t\t Let\'s begin...')
game = input('\n Do you want to play? (yes/no): ').lower()
if game.startswith('y'):
    game = 'y'
else:
    exit()
board = [' '] * 10
display_board(board)
while True:
    turn = first_chance()
    p1, p2 = input_marker()
    print('player ' + str(first_chance()) + ' will go first => ')
    while game == 'y':
        if turn == 1:
            print("\n Player 1\'s turn: ")
            position = player_move('1')
            place_marker(p1, position)
            if check_winner(p1):
                print("\n\n Congratulations Player 1, you won the game!!!!")
                print("\n Better luck next time Player 2 :(")
                break
            if check_tie():
                print("\n Oops! Looks like it's a tie!!")
                break
            else:
                turn = 2
        else:
            print("\n Player 2's turn: ")
            position = player_move('2')
            place_marker(p2, position)
            if check_winner(p2):
                print("\n\n Congratulations Player 2, you won the game!!!!")
                print("\n Better luck next time Player 1 :(")
                break
            if check_tie():
                print("\n Oops! Looks like it's a tie!!")
                break
            else:
                turn = 1
    if not replay():
        print("Goodbye...")
        break