#Tic_Toe

import math

def display_board(board):
    for i in range(0, 9, 3):
        print(f' {board[i]} | {board[i + 1]} | {board[i + 2]}')
        if i < 6:
            print('-' * 9)

def check_win(board, player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_tie(board):
    return ' ' not in board

def minimax(board, depth, alpha, beta, is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, alpha, beta, False)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
            alpha = max(alpha, move_val)

    return best_move

board = [' ' for _ in range(9)]
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

current_player = 'X'

while True:
    display_board(board)

    if current_player == 'X':
        position = int(input(f"Player {current_player}, enter your position (1-9): ")) - 1
        if board[position] == ' ':
            board[position] = current_player
        else:
            print('That position is already taken. Try again.')
            continue
    else:
        if ' ' in board:
            position = find_best_move(board)
            board[position] = current_player

    if check_win(board, 'X'):
        display_board(board)
        print(f'Player {current_player} wins!')
        break
    elif check_win(board, 'O'):
        display_board(board)
        print('AI wins!')
        break
    elif check_tie(board):
        display_board(board)
        print('It\'s a tie!')
        break

    current_player = 'O' if current_player == 'X' else 'X'
