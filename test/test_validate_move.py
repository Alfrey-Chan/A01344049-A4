from unittest import TestCase
from board.board import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_out_of_bounds_south(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        chosen_direction = 'S'
        actual = validate_move(character, chosen_direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_out_of_bounds_north(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 4}
        chosen_direction = 'W'
        actual = validate_move(character, chosen_direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_out_of_bounds_west(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        chosen_direction = 'A'
        actual = validate_move(character, chosen_direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_out_of_bounds_east(self):
        character = {'X-coordinate': 4, 'Y-coordinate': 0}
        chosen_direction = 'D'
        actual = validate_move(character, chosen_direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_obstacle_present(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        chosen_direction = 'W'
        actual = validate_move(character, chosen_direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_is_valid(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        chosen_direction = 'D'
        actual = validate_move(character, chosen_direction)
        expected = True
        self.assertEqual(expected, actual)

