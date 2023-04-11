import io
from unittest import TestCase
from unittest.mock import patch
from character.character import check_if_level_up


class TestCheckIfLevelUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_level_up_no_advance(self, mock_output):
        character_stats = {'level': 1, 'XP': 0, 'skills': {'strength': 1, 'agility': 1, 'luck': 1}}
        leveled_up = check_if_level_up(character_stats)
        actual = mock_output.getvalue()
        expected = "XP to next level: 100\n\n"
        self.assertEqual(expected, actual)
        self.assertFalse(leveled_up)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_level_advance_level(self, mock_output):
        character_stats = {'level': 1, 'XP': 125, 'skills': {'strength': 1, 'agility': 1, 'luck': 1}}
        leveled_up = check_if_level_up(character_stats)
        actual = mock_output.getvalue()
        expected = "XP to next level: 175\n\n"
        self.assertEqual(expected, actual)
        self.assertTrue(leveled_up)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_if_level_max_level(self, mock_output):
        character_stats = {'level': 3, 'XP': 500, 'skills': {'strength': 1, 'agility': 1, 'luck': 1}}
        leveled_up = check_if_level_up(character_stats)
        actual = mock_output.getvalue()
        expected = "Max level reached!\n"
        self.assertEqual(expected, actual)
        self.assertFalse(leveled_up)
