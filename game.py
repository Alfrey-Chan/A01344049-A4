"""
Alfrey Chan
A01344049
"""
from board.board import make_board, set_descriptions, describe_current_location, get_user_choice, validate_move
from board.board import move_character
from combat.combat import check_for_enemies
from character.create_character import create_character


def game():
    board = make_board()
    # board = set_descriptions(board)
    character = create_character()
    # print(character)
    # print(location_descriptions)
    # character = make_character("Player name")

    achieved_goal = False
    print(describe_current_location(board, character))
    while not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            print(describe_current_location(board, character))
            enemy_spawn = check_for_enemies(character)
            if enemy_spawn:
                print(f"A wild {enemy_spawn[0]} appeared!")

        else:
            print("This direction is blocked by rubble and debris, you'll need to find another way around.")
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
