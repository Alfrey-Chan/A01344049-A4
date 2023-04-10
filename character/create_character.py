"""
Alfrey Chan
A01340049
"""


def update_skills(character: dict) -> dict:
    """
    Update values in the character's 'skills' sub-dictionary upon leveling up.

    :param character: a dict containing the character's attributes
    :precondition: character must contain the 'skills' sub-dictionary with the keys 'strength', 'agility', 'luck' and
                   each of these keys have integer values
    :postcondition: updates character's value stored in the chosen key within the 'skills' sub-dictionary by one
    :return: the updated character dict
    """
    print(f"{character['skills']}\nYou've earned a skill point! Which skill would you like to add a point to?")
    choices = f"\t'1' for strength\n\t'2' for agility\n\t'3' for luck"
    skill_map = {1: 'strength', 2: 'agility', 3: 'luck'}
    while True:
        try:
            choice = int(input(f"Pick one of the following:\n{choices}"))
            character['skills'][skill_map[choice]] += 1
            break
        except (ValueError, KeyError):
            print("Invalid input! Please try again.")

    return character


def check_if_level_up(character: dict) -> bool:
    if character['XP'] < 100:
        print(f"XP to next level: {100 - character['XP']}\n")
        return False
    elif character['XP'] >= 100 and character['level'] == 1:
        character['level'] += 1
        print(f"XP to next level: {300 - character['XP']}\n")
        return True
    elif character['XP'] >= 300 and character['level'] == 2:
        character['level'] += 1
        return True
    elif character['XP'] >= 100 and character['level'] == 2:
        print(f"XP to next level: {300 - character['XP']}\n")
        return False
    else:
        print("Max level reached!")
        return False


def update_xp(character: dict, xp_gained: int) -> dict:
    """
    Update the character's XP and level, and also skills if necessary.

    :param character: a dict containing the character's attributes
    :param xp_gained: an int representing the amount of XP gained
    :precondition: character must contain 'XP' and 'level' keys with integer values
    :precondition: xp_gained must be a positive integer
    :postcondition: increases the character's total XP, and also the values stored in the 'skills' sub-dictionary if
                    necessary
    :return: an updated character dict
    """
    character['XP'] += xp_gained
    return character


def create_character() -> dict:
    """
    Create a new character dictionary with default values.

    :return: a dict containing character attributes
    """
    character = {
        'X-coordinate': 0,
        'Y-coordinate': 0,
        'HP': 100,
        'radiation': 0,
        'level': 1,
        'XP': 0,
        'skills': {'strength': 1, 'agility': 1, 'luck': 1}
    }
    return character


def main():
    pass


if __name__ == "__main__":
    main()
