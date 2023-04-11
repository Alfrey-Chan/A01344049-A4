from unittest import TestCase
from board.board import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_check_if_goal_attained_true(self):
        game_map = {(0, 0): "", (0, 1): "", (0, 2): "", (1, 0): "", (2, 2): "endpoint"}
        character_coordinates = {'X-coordinate': 2, 'Y-coordinate': 2}
        actual = check_if_goal_attained(game_map, character_coordinates)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_false(self):
        game_map = {(0, 0): "", (0, 1): "", (0, 2): "", (1, 0): "", (4, 4): "endpoint"}
        character_coordinates = {'X-coordinate': 2, 'Y-coordinate': 2}
        actual = check_if_goal_attained(game_map, character_coordinates)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_index_error(self):
        with self.assertRaises(IndexError):
            game_map = {}
            character_coordinates = {'X-coordinate': 2, 'Y-coordinate': 2}
            check_if_goal_attained(game_map, character_coordinates)

    def test_check_if_goal_attained_key_error(self):
        with self.assertRaises(KeyError):
            game_map = {(0, 0): "", (0, 1): "", (0, 2): "", (1, 0): "", (4, 4): "endpoint"}
            character_coordinates = {'invalid key': 10, 'Y-coordinate': 5}
            check_if_goal_attained(game_map, character_coordinates)

