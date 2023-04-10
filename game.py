"""
Alfrey Chan
A01344049
"""
import itertools
from board.board import set_descriptions, describe_current_location, get_user_choice, validate_move
from board.board import move_character, check_if_goal_attained
from board.enemy_spawn import check_for_enemies
from combat.combat import battle
from character.create_character import create_character, update_xp, check_if_level_up, update_skills


def game():
    board = {(x_coordinate, y_coordinate): None for x_coordinate, y_coordinate in itertools.product(range(5), repeat=2)}
    board = set_descriptions(board)
    character = create_character()
    achieved_goal = False
    print(describe_current_location(board, character))
    while not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            character['radiation'] += 2
            print(describe_current_location(board, character))
            enemy_spawned = check_for_enemies(character)

            if enemy_spawned:
                print(f"A wild {enemy_spawned[0]} appeared!\n")
                battle(character, enemy_spawned)
                if character['HP'] == 0:
                    return print(f"You've been slayed by the mighty {enemy_spawned[0]}")
                update_xp(character, enemy_spawned[1]['XP'])
                leveled_up = check_if_level_up(character)

                if leveled_up:
                    update_skills(character)

                coordinates = ['X-coordinate', 'Y-coordinate']
                character_without_coordinates = {key: value for key, value in character.items() if
                                                 key not in coordinates}
                print(character_without_coordinates)
        else:
            print("This direction is blocked by rubble and debris, you'll need to find another way around.")

        if character['HP'] == 0:
            return print("You've fallen victim to the wasteland...\nGAME OVER")
        if character['radiation'] >= 100:
            return print("You've died from radiation poisoning...\nGAME OVER")
        achieved_goal = check_if_goal_attained(board, character)
    print("You've escaped the wretched wasteland!.... for now.")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
