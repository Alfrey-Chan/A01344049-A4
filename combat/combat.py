"""
Alfrey Chan
A01344049
"""
import random


def chance_game(numbers: list):
    if random.choice(numbers) == 1:
        return True
    return False


def flee(agility: int) -> bool:
    avoid_damage_chance = {
        1: chance_game(list(range(10))),
        2: chance_game(list(range(3))),
        3: chance_game(list(range(2))),
    }
    flee_successful = avoid_damage_chance[agility]
    if flee_successful:
        print("Thanks to your shiftiness, you managed to flee with no injuries.")
        return False
    else:
        print("You find yourself too slow to escape from the enemy. You are forced to fight.")
        return True


def is_jesus(character):
    if character['skills']['luck'] == 3:
        win_game = chance_game([1, 1, 1, 1, 0])
        if win_game:
            print("You feel the lucky charms soaring through your veins!\nYour HP has been restored and your radiation "
                  "levels have been reduced to zero!\n")
            character['HP'] = 100
            character['radiation'] = 0
            coordinates = ['X-coordinate', 'Y-coordinate']
            character_without_coordinates = {key: value for key, value in character.items() if key not in coordinates}
            print(character_without_coordinates)


def attack(character_stats, foe_damage):
    strength_level = character_stats['skills']['strength']
    damage_reduction = {
        1: 1,
        2: 3,
        3: 2
    }
    print("You've defeated the opponent! But you've taken some damage in return.\n")
    character_stats['HP'] = character_stats['HP'] - round(foe_damage/damage_reduction[strength_level])


def battle(character, foe):
    is_jesus(character)
    while True:
        try:
            flee_or_attack = int(input("Would you like to battle or take your chances and flee? \n"
                                       "\tChoose one:\n\t'1' to battle\n\t'2' to flee\n").strip())
            if flee_or_attack not in [1, 2]:
                raise ValueError

            if flee_or_attack == 1:
                attack(character, foe[1]['damage'])
            else:
                flee_unsuccessful = flee(character['skills']['agility'])
                if flee_unsuccessful:
                    attack(character, foe[1]['damage'])
            break
        except ValueError:
            print("Enter a valid input!")

    return character


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
            ('super mutant', {'XP': 0, 'damage': 15}),
            ('deathclaw', {'XP': 0, 'damage': 20}),
            ('fire ant warrior', {'XP': 0, 'damage': 18}),
            ('berserk raider', {'XP': 0, 'damage': 15}),
            ('mutant hound', {'XP': 0, 'damage': 17})
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
