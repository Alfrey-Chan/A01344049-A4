from unittest import TestCase
from board.board import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_south(self):
        character_information = {'X-coordinate': 0, 'Y-coordinate': 2}
        chosen_direction = 'S'
        actual = move_character(character_information, chosen_direction)
        expected = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(expected, actual)

    def test_move_character_north(self):
        character_information = {'X-coordinate': 0, 'Y-coordinate': 0}
        chosen_direction = 'W'
        actual = move_character(character_information, chosen_direction)
        expected = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        character_information = {'X-coordinate': 4, 'Y-coordinate': 0}
        chosen_direction = 'A'
        actual = move_character(character_information, chosen_direction)
        expected = {'X-coordinate': 3, 'Y-coordinate': 0}
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character_information = {'X-coordinate': 0, 'Y-coordinate': 4}
        chosen_direction = 'D'
        actual = move_character(character_information, chosen_direction)
        expected = {'X-coordinate': 1, 'Y-coordinate': 4}
        self.assertEqual(expected, actual)
