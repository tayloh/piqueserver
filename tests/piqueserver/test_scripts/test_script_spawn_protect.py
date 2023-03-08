import unittest
from unittest.mock import MagicMock

import piqueserver.scripts.spawn_protect as spawn_protect


import piqueserver.scripts.blockinfo as blockinfo

from piqueserver.player import FeatureConnection
from piqueserver.server import FeatureProtocol

class BaseSpawnProtectTest(unittest.TestCase):

    def test_spawn_and_hit(self):

        hit_ply = MagicMock()
        hit_ply.spawn_timestamp = -10

        not_hit_ply = MagicMock()
        not_hit_ply.spawn_timestamp = 0

        connection = FeatureConnection
        protocol = FeatureProtocol


        spawn_protocol, spawn_connection =  spawn_protect.apply_script(protocol, connection, None)

        spawn_connection.protocol = MagicMock()
        spawn_connection.on_spawn(spawn_connection, MagicMock())

        self.assertFalse(spawn_connection.on_hit(MagicMock(), 10, not_hit_ply, MagicMock(), MagicMock()))