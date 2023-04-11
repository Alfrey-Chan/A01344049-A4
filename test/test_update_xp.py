from unittest import TestCase
from character.character import update_xp


class TestUpdateXP(TestCase):
    def test_update_xp_gain_xp(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'XP': 0}
        actual = update_xp(character, 75)
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'XP': 75}
        self.assertEqual(expected, actual)

    def test_update_xp_no_xp(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'XP': 100}
        actual = update_xp(character, 0)
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'XP': 100}
        self.assertEqual(expected, actual)
