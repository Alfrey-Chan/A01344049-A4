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


def fight_or_flee() -> int:
    """
    Prompt the user to choose whether to fight or flee.

    :return: user's decision as an integer (1 for fight, 2 for flee)
    """
    while True:
        try:
            decision = int(input("Would you like to battle or take your chances and flee? \n"
                                 "\tChoose one:\n\t'1' to battle\n\t'2' to flee\n").strip())
            if decision not in [1, 2]:
                raise ValueError
            return decision
        except ValueError:
            print("Invalid choice. Please choose again.")


def battle(character, foe: tuple) -> dict:
    """
    Initiate battle between the character and a foe.

    A function that prompts the user to choose to fight or flee, and invokes other functions based on the input.

    :param character: a dict with character attributes
    :param foe: a tuple with foe attributes
    :precondition: character must be a dict with a 'skills' sub-dict that has the 'agility' key
    :precondition: foe must be a tuple with a dict containing the key 'damage' as the second item
    :postcondition: returns updated character dict
    :return: updated character dict
    """
    def is_jesus(character_stats) -> None:
        """
        Check if the character has a luck level of 3.

        A function to invoke the 'chance_game()' to play a game if the character has a luck level of 3. If the character
        wins, the character's 'HP' is restored to 100 and their 'radiation' level is set to 0.

        :param character_stats: a dict containing the character's attributes
        :precondition: character_stats must be a dict with a 'skills' sub-dictionary that has the 'luck' key
        :postcondition: updates the 'HP' and 'radiation' values in the character_stats if 'chance_game()'
                        returns True
        """
        if character_stats['skills']['luck'] == 3:
            win_game = chance_game([1, 1, 1, 1, 0])
            if win_game:
                print(
                    "You feel the lucky charms soaring through your veins!\nYour HP has been restored and your "
                    "radiation levels have been reduced to zero!\n")
                character_stats['HP'] = 100
                character_stats['radiation'] = 0
                coordinates = ['X-coordinate', 'Y-coordinate']
                character_without_coordinates = {key: value for key, value in character_stats.items() if
                                                 key not in coordinates}
                print(character_without_coordinates)

    def attack(character_stats: dict, foe_damage: int) -> None:
        """
        Calculate the damage taken by the character in a battle.

        A function to decrease the character's 'HP' based off the 'strength' attribute of the character by a factor
        based off the values in the 'damage_reduction' dictionary.

        :param character_stats: a dictionary containing the character's attributes
        :param foe_damage: an integer representing the damage dealt by the foe
        :precondition: character_stats must be a dictionary with a 'skills' sub-dictionary that has the 'strength' key
        :precondition: foe_damage must be an integer
        :postcondition: update the incoming foe_damage based on the character's 'strength' attribute and the
                        'damage_reduction' dictionary, and subtract the character's 'HP' by this value
        """
        strength_level = character_stats['skills']['strength']
        damage_reduction = {
            1: 1,
            2: 3,
            3: 2
        }
        print("You've defeated the opponent! But you've taken some damage in return.")
        character_stats['HP'] = character_stats['HP'] - round(foe_damage / damage_reduction[strength_level])

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

    is_jesus(character)
    decision = fight_or_flee()
    if decision == 1:
        attack(character, foe[1]['damage'])
    else:
        flee_unsuccessful = flee(character['skills']['agility'])
        if flee_unsuccessful:
            attack(character, foe[1]['damage'])

    return character


def main():
    pass


if __name__ == "__main__":
    main()
