import io
from unittest import TestCase
from combat.combat import battle
from unittest.mock import patch


class TestBattle(TestCase):
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_not_jesus_and_choice_1(self, mock_output, _):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 0,
            'HP': 100,
            'radiation': 0,
            'level': 1,
            'XP': 0,
            'skills': {'strength': 1, 'agility': 1, 'luck': 1}
        }
        foe = ('Goblin', {'HP': 5, 'damage': 10})
        battle(character, foe)
        actual = mock_output.getvalue()
        expected = "You've defeated the opponent! But you've taken some damage in return.\n"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    @patch('random.choice', return_value=True)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_not_jesus_and_choice_2_escaped_enemy(self, mock_output, _, __):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 0,
            'HP': 100,
            'radiation': 0,
            'level': 3,
            'XP': 0,
            'skills': {'strength': 1, 'agility': 1, 'luck': 1}
        }
        foe = ('Goblin', {'HP': 5, 'damage': 10})
        battle(character, foe)
        actual = mock_output.getvalue()
        expected = "Thanks to your shiftiness, you managed to flee with no injuries.\n"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    @patch('random.choice', return_value=False)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_not_jesus_and_choice_2_failed_escape(self, mock_output, _, __):
        character = {
            'X-coordinate': 1,
            'Y-coordinate': 1,
            'HP': 100,
            'radiation': 0,
            'level': 3,
            'XP': 0,
            'skills': {'strength': 1, 'agility': 1, 'luck': 1}
        }
        foe = ('Goblin', {'HP': 5, 'damage': 10})
        battle(character, foe)
        actual = mock_output.getvalue()
        expected = "You find yourself too slow to escape from the enemy. You are forced to fight.\n"\
                   "You've defeated the opponent! But you've taken some damage in return.\n"
        self.assertEqual(expected, actual)

