"""
Alfrey Chan
A01344049
"""
import random


def check_for_enemies(character: dict) -> tuple:
    """
    Check for enemy spawns in the current location.

    A function to return a foe tuple containing its name, 'XP' value, and 'damage' value if the character is present at
    a special location, or if a random number generator the int 1 at an estimated 33% chance.

    :param character: a dict containing the character's attributes
    :precondition: character must be a dict containing the keys 'X-coordinate', 'Y-coordinate' and 'level'
    :postcondition: returns a foe tuple containing its name, 'XP' value, and 'damage' value
    :return: a tuple
    """
    def spawn_special_foe(location: tuple, special_foes: dict) -> tuple:
        """
        Generate a special foe for a given location.

        The function to look up the special foe associated with the given 'location' in the 'special_foes' dictionary
        and return a tuple containing the foe's name and attributes.

        :param location: a tuple containing the coordinates of the special spawn point
        :param special_foes: a dict containing the special spawn points and their associated foes
        :precondition: location must be a (x, y) tuple where x and y are positive integers
        :precondition: special_foes must be a dictionary containing (x, y) a tuple coordinate as keys, and a tuple
                       containing the foe's information
        :postcondition: Returns a tuple containing a special foe name and a special foe dictionary containing the foe's
                        attributes
        :return: a tuple
        """
        special_foe = special_foes[location]
        return special_foe

    special_spawns = {
        (4, 0): ('barely sane man', {'XP': 50, 'damage': 5}),
        (2, 1): ('ghoul cluster', {'XP': 75, 'damage': 15}),
        (0, 3): ('mutant behemoth', {'XP': 100, 'damage': 30}),
        (4, 4): ('deathclaw queen', {'XP': 0, 'damage': 35})
    }
    normal_spawns = {
        1: [
            ('mole rat', {'XP': 7, 'damage': 2}),
            ('fire ant', {'XP': 9, 'damage': 4}),
            ('stinger', {'XP': 20, 'damage': 4}),
            ('radiated roach', {'XP': 10, 'damage': 2}),
            ('mutated python', {'XP': 6, 'damage': 6})
        ],
        2: [
            ('feral ghoul', {'XP': 25, 'damage': 8}),
            ('radscorpion', {'XP': 40, 'damage': 10}),
            ('glowing ghoul', {'XP': 35, 'damage': 10}),
            ('soul seeker', {'XP': 45, 'damage': 12}),
            ('psycho scavenger', {'XP': 30, 'damage': 13})
        ],
        3: [
            ('super mutant', {'XP': 150, 'damage': 15}),
            ('deathclaw', {'XP': 200, 'damage': 20}),
            ('fire ant warrior', {'XP': 150, 'damage': 18}),
            ('berserk raider', {'XP': 150, 'damage': 15}),
            ('mutant hound', {'XP': 150, 'damage': 17})
        ]
    }
    special_spawn_locations = {(4, 0), (2, 1), (0, 3), (4, 4)}
    current_location = (character['X-coordinate'], character['Y-coordinate'])
    current_level = character['level']

    if current_location in special_spawn_locations:
        return spawn_special_foe(current_location, special_spawns)
    else:
        if random.choice([1, 2, 3]) == 1:
            return random.choice(normal_spawns[current_level])


def main():
    pass


if __name__ == "__main__":
    main()
