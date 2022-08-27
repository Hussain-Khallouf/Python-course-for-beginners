# import random


def instructions():
    print("Welcome to the Tic Tac Toe Game!")
    print("Rules are Simple")
    print("The play ground is just like this : \n")
    print("1 | 2 | 3")
    print("----------")
    print("4 | 5 | 6")
    print("----------")
    print("7 | 8 | 9\n\n")
    print("Each player in his turn enter the number of the wanted cell")
    print("The winner is the one who can get 3 in a row or column or diagonal")
    print("First Player will be choosen randomly and he will choose to be X or O")
    print("Have Fun!\n\n")


def print_board(board):

    print("{} | {} | {}            1 | 2 | 3".format(board[0], board[1], board[2]))
    print("-----------          ---------")
    print("{} | {} | {}            4 | 5 | 6".format(board[3], board[4], board[5]))
    print("-----------          ---------")
    print("{} | {} | {}            7 | 8 | 9".format(board[6], board[7], board[8]))


def def_first_player():
    """
    define who plays first and what marker he wants
    return: rand: which player palys first
    raturn: player1 marker (X or O)
    return: player2 marker (X or O)
    """
    rand = 0
    player1_marker = "-"
    player2_marker = "-"
    while player1_marker != "X" and player1_marker != "O":
        player1_marker = input("Player 1: choose marker X, O: ")
        if player1_marker == "X":
            player2_marker = "O"
        else:
            player2_marker = "X"
    return rand, player1_marker, player2_marker


def check_valid(board, index):
    """
    check if an specific cell is empty
    """
    return board[index] == "-"


def place_marker(board, index, marker):
    while index < 1 or index > 9 or not check_valid(board, index - 1):
        index = input("invalid cell, please try again  ")
        index = int(index)
    board[index - 1] = marker


def check_win(board):
    winning_cases = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for t1, t2, t3 in winning_cases:
        if board[t1] == board[t2] == board[t3] and board[t1] != "-":
            return True
    return False


def check_tie(board):
    return "-" not in board


def game_over(board):
    if check_win(board):
        return 1
    if check_tie(board):
        return 0
    return -1


instructions()

board = ["-"] * 9
turn, player1_marker, player2_marker = def_first_player()


while True:
    # for each player turn
    if turn == 0:
        index = int(input("Player1, Choose your next position: (1-9) "))
        place_marker(board, index, player1_marker)
    if turn == 1:
        index = int(input("Player2, Choose your next position: (1-9) "))
        place_marker(board, index, player2_marker)

    print_board(board)

    result = game_over(board)
    if result == 1:
        if turn == 0:
            print("Congratulations! Player1 have won the game!")
        else:
            print("Congratulations! Player2 have won the game!")
        break
    if result == 0:
        print("The game is a draw!")
        break
    else:
        # reversing the turn so it will take values (1 and 0 only)
        # not(1) = 0
        # not(0) = 1
        turn = int(not turn)
