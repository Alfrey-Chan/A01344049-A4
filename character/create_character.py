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


def update_xp(character, xp_gained: int) -> dict:
    def check_if_level_up() -> bool:
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
            character['level'] = 'max'
            return False

    character['XP'] += xp_gained
    if check_if_level_up() is True:
        update_skills(character)

    coordinates = ['X-coordinate', 'Y-coordinate']
    character_without_coordinates = {key: value for key, value in character.items() if key not in coordinates}
    print(character_without_coordinates)
    return character


def create_character():
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
