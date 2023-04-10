"""
Alfrey Chan
A01344049
"""
import random


def check_for_enemies(character):
    def spawn_special_foe(location: tuple, special_foes: dict) -> tuple:
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
