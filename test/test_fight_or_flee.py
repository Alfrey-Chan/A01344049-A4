from unittest import TestCase
from combat.combat import fight_or_flee
from unittest.mock import patch
import io


class TestFightOrFlee(TestCase):
    @patch('builtins.input', return_value='1')
    def test_fight_or_flee_user_enters_1(self, _):
        expected = 1
        actual = fight_or_flee()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_fight_or_flee_user_enters_2(self, _):
        expected = 2
        actual = fight_or_flee()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['some incorrect input', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_user_enters_invalid_input(self, mock_output, _):
        fight_or_flee()
        expected = "Invalid choice. Please choose again.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)