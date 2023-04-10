"""
Alfrey Chan
A01344049
"""
import random


def chance_game(numbers: list) -> bool:
    """
    Return True if the number 1 is randomly selected from the given list.

    :param numbers: a list
    :precondition: numbers must be a non-empty list
    :precondition: numbers must contain more than one element, with one being at least the integer 1
    :postcondition: returns True if the number 1 is randomly selected from the list, else False
    :return: True or False
    """
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
    print("You've defeated the opponent! But you've taken some damage in return.")
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


def main():
    pass


if __name__ == "__main__":
    main()
