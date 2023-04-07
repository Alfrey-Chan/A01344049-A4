"""
Alfrey Chan
A01344049
"""
from board.board import make_board
from board.board import set_descriptions


def game():
    board = make_board()
    location_descriptions = set_descriptions(board)
    # print(location_descriptions)

    # character = make_character("Player name")
    # achieved_goal = False
    # while not achieved_goal:
    #
    # describe_current_location(board, character)
    # direction = get_user_choice()
    # valid_move = validate_move(board, character, direction)
    # if valid_move:
    #     move_character(character)
    # describe_current_location(board, character)
    # there_is_a_challenge = check_for_challenges()
    # if there_is_a_challenge:
    #     execute_challenge_protocol(character)
    # if character_has_leveled():
    #     execute_glow_up_protocol()
    # achieved_goal = check_if_goal_attained(board, character)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()