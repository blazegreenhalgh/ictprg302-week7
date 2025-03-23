"""A tic-tac-toe game to practice dictionaries
and code reading
Users shall be presented with this board:
  a   b   c
1 - | - | -
2 - | - | -
3 - | - | -
(1) For a given input, say "1, a", use a translation
dictionary to translate to coordinates (say 0, 0)
"""
translation = {"cols": {"a": 0, "b": 1, "c": 2},  # TODO: Complete me
               "rows": {"1": 0, "2": 1, "3": 2}
               }

players = {"x_player": {"name": '',
                        "symbol": 'X',
                        "wins": 0,
                        "draws": 0,
                        "losses": 0},
           "o_player": {"name": '',
                        "symbol": 'O',
                        "wins": 0,
                        "draws": 0,
                        "losses": 0},
           "current_player": ''}  # TODO: Use me!

WINS = [  # lists all win conditions for 3 x 3 board
    [(0, 0), (1, 1), (2, 2)],  # diag 1
    [(0, 2), (1, 1), (2, 0)],  # diag 2
    [(0, 0), (0, 1), (0, 2)],  # row 1
    [(1, 0), (1, 1), (1, 2)],  # row 2
    [(2, 0), (2, 1), (2, 2)],  # row 3
    [(0, 0), (1, 0), (2, 0)],  # col a
    [(0, 1), (1, 1), (2, 1)],  # col b
    [(0, 2), (1, 2), (2, 2)],  # col c
]


# Optional task (challenging): generate the above list dynamically using for loops.


def create_board():
    return [['-' for _ in range(3)]
            for _ in range(3)]


def print_board(board):
    print("  a   b   c")
    for i, row in enumerate(board, 1):
        print(i, end=' ')
        print(' | '.join(row))


def translate(row, col):
    """Returns corresponding position from dictionary"""
    # TODO: Finish this function so it returns the correct row, col
    # For example:
    # >>> translate('1', 'a')
    # (0, 0)
    return ...


def has_free_spaces(board):
    for row in board:
        if '-' in row:
            return True
    return False


def is_occupied(board, coords):
    row, col = coords
    return '-' != board[row][col].strip()


def is_winner(x_or_o, board):
    for (row1, col1), (row2, col2), (row3, col3) in WINS:
        if (board[row1][col1] ==
                board[row2][col2] ==
                board[row3][col3] ==
                x_or_o):
            return True
    return False


def switch(current, p1, p2):
    if current == p1:
        return p2
    else:
        return p1


def set_position(x_or_o, board, coords):
    row, col = coords
    board[row][col] = x_or_o.upper()

def play_again():
    if input("Play again? ").lower()[0] == 'y':
        return True
    else:
        return False

def record_scores(winner, p1, p2):
    if winner == p1["name"]:
        p1["wins"] += 1
        p2["losses"] += 1
    elif winner != p1["name"] and winner != p2["name"]:
        p1["draws"] += 1
        p2["draws"] += 1
    else:
        p1["losses"] += 1
        p2["wins"] += 1




def play():
    # DONE : Set player names in the players dictionary
    # DONE : Initialize current_player from the dictionary
    # DONE : Get the player name from the dictionary
    # DONE : Implement switching players using the players dictionary
    player_x = players["x_player"]
    player_o = players["o_player"]

    print("Welcome to Tic-Tac Life!")

    print("What shall I call the 'X' player?")
    player_x["name"] = input("Player X's name> ")
    print("and the 'O' player?")
    player_o["name"] = input("Player O's name> ")

    board = create_board()

    players["current_player"] = player_x["name"]
    current_player = players["current_player"]
    symbol = player_x["symbol"]

    while True:
        print(f"{current_player} make your move:")
        print_board(board)
        move = input("Enter move as row col: ")
        row, col = move.split(' ')
        row, col = translation["rows"][row], translation["cols"][col]  # TODO: populate translation dict - otherwise this fails
        print(row, col)

        if is_occupied(board, (row, col)):
            print("You must pick an unused space")
            continue
        else:
            set_position(symbol, board, (row, col))

        if is_winner(symbol, board):
            print(f"Well done!\n{current_player} wins!")
            record_scores(current_player, player_x, player_o)
            print(players)
            print(current_player)
            print(player_x)
            print(player_o)
            if play_again():
                play()
            else:
                print("Thanks for playing!")
            break

        if not has_free_spaces(board):
            print("It is a draw!")
            record_scores(current_player, player_x, player_o)

            if play_again():
                play()
            else:
                print("Thanks for playing!")
            break

        current_player = switch(current_player, player_x["name"], player_o["name"])
        symbol = switch(symbol, player_x["symbol"], player_o["symbol"])



    # DONE: add ability to play again
    # DONE: keep tally of wins, losses, and draws in the dictionary
    # TODO: print the dictionary as a csv like so:
    # name,symbol,wins,draws,losses
    # fred,X,10,5,3
    # wilma,O,5,10,3
    # BONUS: instead of using csv, write the dictionary to a JSON file
    # (clue: even though it is the bonus question, this is actually easier!)


play()