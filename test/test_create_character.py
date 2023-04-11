from unittest import TestCase
from character.character import create_character


class TestCreateCharacter(TestCase):
    def test_create_character(self):
        actual = create_character()
        expected = character = {
        'X-coordinate': 0,
        'Y-coordinate': 0,
        'HP': 100,
        'radiation': 0,
        'level': 1,
        'XP': 0,
        'skills': {'strength': 1, 'agility': 1, 'luck': 1}
        }
        self.assertEqual(expected, actual)

