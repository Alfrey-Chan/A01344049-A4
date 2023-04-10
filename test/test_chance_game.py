from unittest import TestCase
from unittest.mock import patch
from combat.combat import chance_game


class TestChanceGame(TestCase):
    @patch('random.choice', side_effect=[1])
    def test_chance_game_number_list_true(self, _):
        numbers = [1, 2, 3, 4]
        actual = chance_game(numbers)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[3])
    def test_chance_game_number_list_false(self, _):
        numbers = [1, 2, 3, 4]
        actual = chance_game(numbers)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1])
    def test_chance_game_not_only_numbers_true(self, _):
        random_list = [['apple', 'orange'], 1, ('a', 95), False]
        actual = chance_game(random_list)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[('a', 95)])
    def test_chance_game_not_only_numbers_false(self, _):
        random_list = [['apple', 'orange'], 1, ('a', 95), False]
        actual = chance_game(random_list)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[True])
    def test_chance_game_true_boolean(self, _):
        random_list = [True, 2, 3, 4]
        actual = chance_game(random_list)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[False])
    def test_chance_game_false_boolean(self, _):
        random_list = [False, 1,  2, 3, 4]
        actual = chance_game(random_list)
        expected = False
        self.assertEqual(expected, actual)