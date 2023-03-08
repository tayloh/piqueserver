from twisted.trial import unittest
from pyspades import weapon
from unittest.mock import MagicMock

class BaseWeaponTest(unittest.TestCase):
    def test_set_shoot(self):
        wpn = weapon.BaseWeapon.__init__(MagicMock())

        shoot_time = wpn.shoot_time
        wpn.set_shoot(True)
        self.assertTrue(wpn.shoot_time != shoot_time)

        next_shot = wpn.next_shot
        wpn.set_shoot(False)
        self.assertTrue(wpn.next_shot != next_shot)
