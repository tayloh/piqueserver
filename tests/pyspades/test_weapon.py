from twisted.trial import unittest
from pyspades import weapon
from unittest.mock import Mock

class BaseWeaponTest(unittest.TestCase):
    def test_set_shoot(self):
        wpn = weapon.BaseWeapon.__init__(Mock())

        shoot_time = wpn.shoot_time
        wpn.set_shoot(True)
        self.assertNotEqual(wpn.shoot_time, shoot_time)
        next_shot = wpn.next_shot
        wpn.set_shoot(False)
        self.assertNotEqual(wpn.next_shot, next_shot)
