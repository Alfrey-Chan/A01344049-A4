import io
from unittest import TestCase
from unittest.mock import patch
from character.character import update_skills


class TestUpdateSkills(TestCase):
    @patch('builtins.input', return_value='3')
    def test_update_skills_luck(self, _):
        character_stats = {'level': 2, 'XP': 125, 'skills': {'strength': 1, 'agility': 1, 'luck': 1}}
        actual = update_skills(character_stats)
        expected = {'level': 2, 'XP': 125, 'skills': {'strength': 1, 'agility': 1, 'luck': 2}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_update_skills_agility(self, _):
        character_stats = {'level': 3, 'XP': 500, 'skills': {'strength': 1, 'agility': 2, 'luck': 1}}
        actual = update_skills(character_stats)
        expected = {'level': 3, 'XP': 500, 'skills': {'strength': 1, 'agility': 3, 'luck': 1}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='1')
    def test_update_skills_strength(self, _):
        character_stats = {'level': 2, 'XP': 125, 'skills': {'strength': 1, 'agility': 1, 'luck': 1}}
        actual = update_skills(character_stats)
        expected = {'level': 2, 'XP': 125, 'skills': {'strength': 2, 'agility': 1, 'luck': 1}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['some invalid input', 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_skills_catch_error(self, mock_output, _):
        character_stats = {'level': 1, 'XP': 100, 'skills': {'strength': 1, 'agility': 1, 'luck': 1}}
        update_skills(character_stats)
        actual = mock_output.getvalue()
        expected = "{'strength': 1, 'agility': 1, 'luck': 1}\nYou've earned a skill point! Which skill would you like "\
                   "to add a point to?\nInvalid input! Please try again.\n"
        self.assertEqual(expected, actual)
