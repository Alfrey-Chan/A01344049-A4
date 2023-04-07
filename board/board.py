"""
Alfrey Chan
A01344049
"""
import itertools
import random


def set_descriptions(board):
    def randomized_descriptions(game_map):
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
    return board
