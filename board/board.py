"""
Alfrey Chan
A01344049
"""
import itertools
import random


def check_if_goal_attained(board: dict, character: dict) -> bool:
    """
    Check if the player has reached the endpoint of the game.

    A function that checks if the character coordinates match the endpoint coordinates of a board.

    :param board: a dict with tuples as keys representing coordinates of a map
    :param character: a dict with character attributes and coordinates of the current location
    :precondition: board must be a non-empty dict with (x, y) tuple keys representing x and y coordinates
    :precondition: the endpoint coordinates in board must be the last item in the list of keys
    :precondition: character must contain the keys 'X-coordinate' and 'Y-coordinate' each with single int value
    :postcondition: returns True if the coordinates of the character match the last key of the dict board, else False
    :return: True or False
    :raises KeyError: if character dict does not contain the keys 'X-coordinate' and 'Y-coordinate'
    :raises IndexError: if board dict is empty of the list of keys are empty
    >>> game_map = {(0, 0): "", (0, 1): "", (0, 2): "", (1, 0): "", (2, 2): "endpoint"}
    >>> character_coordinates = {'X-coordinate': 2, 'Y-coordinate': 2}
    >>> check_if_goal_attained(game_map, character_coordinates)
    True
    >>> game_map = {(0, 0): "", (0, 1): "", (0, 2): "", (1, 0): "", (2, 2): "endpoint"}
    >>> character_coordinates = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> check_if_goal_attained(game_map, character_coordinates)
    False
    >>> game_map = {(0, 0): "", (0, 1): "", (0, 2): "", (1, 0): "", (2, 2): "endpoint"}
    >>> character_coordinates = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> check_if_goal_attained(game_map, character_coordinates)
    False
    """
    goal_destination = list(board.keys())[-1]
    if (character['X-coordinate'], character['Y-coordinate']) == goal_destination:
        return True
    return False


def move_character(character: dict, direction: str) -> dict:
    """
    Move the character one unit by the specified direction.

    A function to update the value of the key 'X-coordinate' or 'Y-coordinate' in character_coordinates depending on
    the selected choice of direction.

    :param character: a dict with character attributes and coordinates of the current location
    :param direction: a string representing the player's choice of direction
    :precondition: character must contain the keys 'X-coordinate' and 'Y-coordinate' each with single int value
    :precondition: direction must be one of the following single character strings: 'W', 'A', 'S' or 'D'
    :postcondition: decreases or increases the value belonging to the key 'X-coordinate' or 'Y-coordinate' in the
                    dictionary character depending on the value of direction
    :return: the character dict
    :raises KeyError: if character dict does not contain the keys 'X-coordinate' and 'Y-coordinate'
    >>> character_information = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> chosen_direction = 'S'
    >>> updated_character = move_character(character_information, chosen_direction)
    >>> updated_character
    {'X-coordinate': 0, 'Y-coordinate': -1}
    >>> character_information = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> chosen_direction = 'W'
    >>> updated_character = move_character(character_information, chosen_direction)
    >>> updated_character
    {'X-coordinate': 1, 'Y-coordinate': 2}
    >>> character_information = {'X-coordinate': 2, 'Y-coordinate': 2}
    >>> chosen_direction = 'A'
    >>> updated_character = move_character(character_information, chosen_direction)
    >>> updated_character
    {'X-coordinate': 1, 'Y-coordinate': 2}
    """
    if direction == 'W':
        character["Y-coordinate"] += 1
    elif direction == 'A':
        character["X-coordinate"] -= 1
    elif direction == 'S':
        character["Y-coordinate"] -= 1
    else:
        character["X-coordinate"] += 1
    return character


def validate_move(character: dict, direction: str) -> bool:
    """
    Verify if the chosen direction leads to a coordinate that is out of bounds.

    A function that checks if a move in a specified direction results in a coordinate outside the valid range, defined
    by (x, y), where x and y are integers from 0 to 2.

    :param character: a dictionary representing the character
    :param direction: a string representing the player's choice of direction
    :precondition: character must be a dictionary created by the make_character function
    :precondition: direction must be one of the following strings: 'W', 'A', 'S' or 'D'
    :postcondition: returns False if the 'X-coordinate' is 0 and the chosen direction is 'A', or if the 'X-coordinate'
                    is 2 and the chosen direction is 'D', else True for other cases involving 'X-coordinate'
    :postcondition: returns False if the 'Y-coordinate' is 0 and the chosen direction is 'W', or if the 'Y-coordinate'
                    is 2 and the chosen direction is 'S', else True for other cases involving 'Y-coordinate'
    :return: True or False
    >>> character_details = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> chosen_direction = 'W'
    >>> validate_move(character_details, chosen_direction)
    False
    >>> character_details = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
    >>> chosen_direction = 'D'
    >>> validate_move(character_details, chosen_direction)
    False
    >>> character_details = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
    >>> chosen_direction = 'S'
    >>> validate_move(character_details, chosen_direction)
    True
    """
    possible_moves = {
        (0, 0): ['D'],
        (1, 0): ['D'],
        (2, 0): ['W', 'D'],
        (3, 0): ['D', 'A'],
        (4, 0): ['A'],
        (0, 1): ['W', 'D'],
        (1, 1): ['W', 'D', 'A'],
        (2, 1): ['A', 'S', 'D'],
        (3, 1): ['A', 'D'],
        (4, 1): ['A', 'W'],
        (0, 2): ['S', 'D'],
        (1, 2): ['A', 'S'],
        (2, 2): ['W', 'D'],
        (3, 2): ['A', 'W'],
        (4, 2): ['W', 'S'],
        (0, 3): ['W'],
        (1, 3): ['W', 'D'],
        (2, 3): ['A', 'S'],
        (3, 3): ['S', 'D'],
        (4, 3): ['S', 'A'],
        (0, 4): ['S', 'D'],
        (1, 4): ['S', 'A', 'D'],
        (2, 4): ['A', 'D'],
        (3, 4): ['A', 'D'],
        (4, 4): ['A']
    }
    player_position = (character['X-coordinate'], character['Y-coordinate'])
    if direction in possible_moves[player_position]:
        return True
    return False


def get_user_choice() -> str:
    """
    Ask user to enter one of the four direction choices.

    :return: a string
    """
    choices = """ 
    'W' for North
    'A' for West
    'S' for South
    'D' for East   
    """
    direction = input(f"Which direction?:\n{choices}").strip().upper()
    print()

    while direction not in ['W', 'A', 'S', 'D']:
        print("Invalid input! Please choose one of the following options:")
        direction = input(f"Choose the direction you'd like to move:\n{choices}").strip().upper()
    return direction


def describe_current_location(board: dict, character: dict) -> dict:
    current_location = (character['X-coordinate'], character['Y-coordinate'])
    return board[current_location]


def set_descriptions(board: dict) -> dict:
    def randomized_descriptions(game_map: dict) -> dict:
        coordinate_descriptions = [
            "Ugh, I don't feel so good...",
            "There's some odd growling noises in the distance. Doesn't sound too inviting...",
            "You stumble over some unrecognizable corpses. Your head is still a bit woozy...",
            "You scan the area around you, but there seems to be no sign of human life...",
            "As I slowly come to my senses, I realize that everything around me is destroyed and unrecognizable...",
            "The ringing in my ears makes is unbearable, but the silence of the wasteland is still deafening...",
            "The acrid smoke burns my throat and stings my eyes...",
            "The rubble and debris make it nearly impossible to move without stumbling...",
            "My heart races as I realize that there might not be anyone else alive around me...",
            "The constant beeping of a nearby destroyed car is the only sound in this desolate wasteland...",
            "The devastation around me is almost too much to bear as I try to take it all in...",
            "The choking dust makes it hard to breathe, and I cough uncontrollably...",
            "The smell of burning buildings and melting metal is nauseating...",
            "The destruction stretches as far as the eye can see, with no signs of life anywhere",
            "My survival instinct kicks in as I start searching for any sign of food or water...",
            "The silence of the wasteland is only broken by the occasional distant explosion...",
            "The foul indescribable smell pollutes the air, as you resist the urge to vomit...",
            "There’s some rattling in the beaten up bushes in the corner...",
            "As I search for any signs of life, my mind can only grasp the scale of destruction that surrounds me...",
            "The once-familiar streets are now unrecognizable, with buildings reduced to rubble and debris...",
            "Twisted metal and rubble of what used to be buildings tower over me, making me feel small...",
            "A sense of dread creeps up on you as you realize you've been walking in circles for hours...",
            "Every step feels like a gamble, with danger lurking around every corner...",
            "The endless expanse of destruction leaves me feeling hopeless and alone...",
            "The air is thick with dust and debris, making it hard to see..."
        ]

        descriptions = random.sample(coordinate_descriptions, len(coordinate_descriptions))
        game_map = {coordinate: description for coordinate, description in zip(list(game_map.keys()), descriptions)}
        return game_map

    board = randomized_descriptions(board)
    return board


def make_board():
    board = {(x_coordinate, y_coordinate): None for x_coordinate, y_coordinate in itertools.product(range(5), repeat=2)}
    return set_descriptions(board)
