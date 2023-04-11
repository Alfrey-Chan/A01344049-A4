from unittest import TestCase
from unittest.mock import patch
from enemy_spawn import check_for_enemies


class TestCheckForEnemies(TestCase):
    @patch('random.choice', return_value=2)
    def test_check_for_enemies_no_spawn_random_number_is_2(self, _):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 1,
            'level': 1
        }
        actual = check_for_enemies(character)
        expected = None
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value=3)
    def test_check_for_enemies_no_spawn_random_number_is_3(self, _):
        character = {
            'X-coordinate': 1,
            'Y-coordinate': 1,
            'level': 1
        }
        actual = check_for_enemies(character)
        expected = None
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('mole rat', {'XP': 7, 'damage': 2})])
    def test_check_for_enemies_spawn_level_1_monster(self, _):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 2,
            'level': 1
        }
        actual = check_for_enemies(character)
        expected = ('mole rat', {'XP': 7, 'damage': 2})
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('psycho scavenger', {'XP': 30, 'damage': 13})])
    def test_check_for_enemies_spawn_level_2_monster(self, _):
        character = {
            'X-coordinate': 2,
            'Y-coordinate': 2,
            'level': 2
        }
        actual = check_for_enemies(character)
        expected = ('psycho scavenger', {'XP': 30, 'damage': 13})
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('super mutant', {'XP': 150, 'damage': 15})])
    def test_check_for_enemies_spawn_level_3_monster(self, _):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 4,
            'level': 3
        }
        actual = check_for_enemies(character)
        expected = ('super mutant', {'XP': 150, 'damage': 15})
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('mutant behemoth', {'XP': 100, 'damage': 30})])
    def test_check_for_enemies_special_spawns_1(self, _):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 3,
            'level': 3
        }
        actual = check_for_enemies(character)
        expected = ('mutant behemoth', {'XP': 100, 'damage': 30})
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('deathclaw queen', {'XP': 0, 'damage': 35})])
    def test_check_for_enemies_special_spawns_2(self, _):
        character = {
            'X-coordinate': 4,
            'Y-coordinate': 4,
            'level': 3
        }
        actual = check_for_enemies(character)
        expected = ('deathclaw queen', {'XP': 0, 'damage': 35})
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('ghoul cluster', {'XP': 75, 'damage': 15})])
    def test_check_for_enemies_special_spawns_3(self, _):
        character = {
            'X-coordinate': 2,
            'Y-coordinate': 1,
            'level': 2
        }
        actual = check_for_enemies(character)
        expected = ('ghoul cluster', {'XP': 75, 'damage': 15})
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[1, ('barely sane man', {'XP': 50, 'damage': 5})])
    def test_check_for_enemies_special_spawns_4(self, _):
        character = {
            'X-coordinate': 4,
            'Y-coordinate': 0,
            'level': 2
        }
        actual = check_for_enemies(character)
        expected = ('barely sane man', {'XP': 50, 'damage': 5})
        self.assertEqual(expected, actual)

