# tictactoe reference solution
#
# Laszlo Molnar, 2016, Codecool
import os

# global variables
table = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
current_player = "X"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_welcome_info():
    print("--- TicTacToe ---\n")
    print("Welcome! The goal of the game is to make three X's or O's in a line.")
    print("The line can be in a column/row or it can be diagonal.\n")


def show_menu():
    print("1. PLAY GAME (2 player)")
    print("2. QUIT\n")


def process_menu_decision():
    user_input = ""
    while (user_input != "1" and user_input != "2"):
        user_input = input(
            "Choose from the numbers (write 1 or 2 and press ENTER): ")
    if "1" == user_input:
        play_two_player_game()
        return 1
    if "2" == user_input:
        print("Bye!")
    return 2


def play_two_player_game():
    init_game()
    global current_player
    current_player = decide_who_starts()
    do_game_loop()
    input("Press ENTER to go back to the Main Menu.")


def init_game():
    global table
    table = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


def decide_who_starts():
    clear_screen()
    who_starts = ""
    while who_starts != "X" and who_starts != "O":
        who_starts = input("'X'or 'O' should start the game (X/O)? ").upper()
    return who_starts


def do_game_loop():
    global table
    draw_table()
    remaining_steps = len(table) * len(table[0])
    game_won = False
    while game_won is False and remaining_steps > 0:
        coords = get_table_coords_from_player()
        while False is coords_are_valid(coords):
            print("The place you chosen is not empty!")
            coords = get_table_coords_from_player()
        global current_player
        table[coords[0]][coords[1]] = current_player
        if True is game_finished(coords):
            game_won = True
        else:
            change_current_player()
        draw_table()
        remaining_steps = remaining_steps - 1
    evaluate_game_ending(game_won)


def draw_table():
    clear_screen()
    print("    A   B   C")
    print("  -------------")
    print("1 |", table[0][0], "|", table[1][0], "|", table[2][0], "|")
    print("  -------------")
    print("2 |", table[0][1], "|", table[1][1], "|", table[2][1], "|")
    print("  -------------")
    print("3 |", table[0][2], "|", table[1][2], "|", table[2][2], "|")
    print("  -------------")


def get_table_coords_from_player():
    coords = (-1, -1)
    while coords[0] == -1 or coords[1] == -1:
        global current_player
        next_move = input("'" + current_player +
                          "', what is your next move(for ex. A2)? ")
        if len(next_move) > 1:
            next_move = next_move.upper()
            coords = parse_player_input(next_move)
    return coords


def parse_player_input(player_input):
    col = -1
    row = -1
    if player_input[0] == 'A':
        col = 0
    if player_input[0] == 'B':
        col = 1
    if player_input[0] == 'C':
        col = 2
    if player_input[1] == '1':
        row = 0
    if player_input[1] == '2':
        row = 1
    if player_input[1] == '3':
        row = 2
    return col, row


def coords_are_valid(coords):
    if table[coords[0]][coords[1]] == ".":
        return True
    return False


def change_current_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def game_finished(last_coord):
    # check if the player won
    global current_player

    # horizontal checking
    start_point = check_same_items(last_coord, (-1, 0))
    end_point = check_same_items(last_coord, (1, 0))
    if end_point[0] - start_point[0] >= 2:
        return True
    # vertical checking
    start_point = check_same_items(last_coord, (0, -1))
    end_point = check_same_items(last_coord, (0, 1))
    if end_point[1] - start_point[1] >= 2:
        return True
    # diagonal - left-to-right checking
    start_point = check_same_items(last_coord, (-1, -1))
    end_point = check_same_items(last_coord, (1, 1))
    if end_point[0] - start_point[0] >= 2:
        return True
    # diagonal - right-to-left checking
    start_point = check_same_items(last_coord, (1, -1))
    end_point = check_same_items(last_coord, (-1, 1))
    if abs(end_point[0] - start_point[0]) >= 2:
        return True

    return False


def check_same_items(start_coord, inc_coord):
    final_coord = start_coord
    next_coord = (final_coord[0] + inc_coord[0], final_coord[1] + inc_coord[1])

    while next_coord[0] >= 0 and next_coord[0] <= 2 and \
            next_coord[1] >= 0 and next_coord[1] <= 2 and \
            table[next_coord[0]][next_coord[1]] == current_player:
        final_coord = next_coord
        next_coord = (next_coord[0] + inc_coord[0],
                      next_coord[1] + inc_coord[1])
    return final_coord


def evaluate_game_ending(game_won):
    if game_won is True:
        print("'" + current_player + "' won the game!")
    else:
        print("It's a draw!")

# main
menu_decision = 0
while menu_decision != 2:
    clear_screen()
    show_welcome_info()
    show_menu()
    menu_decision = process_menu_decision()
