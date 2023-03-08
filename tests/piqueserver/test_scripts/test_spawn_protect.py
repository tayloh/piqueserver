from twisted.trial import unittest
from piqueserver import spawn_protect, player
from unittest.mock import Mock

class BaseSpawnProtectTest(unittest.TestCase):
    connection = FeatureConnection
    protocol = FeatureProtocol
    spawn_protocol, spawn_connection = spawn_protect.apply_script(protocol, connection, None)

    hit_ply = player.ServerConnection(Mock(), Mock())
    hit_ply.spawn_timestamp = 0

    spawn_connection.on_spawn(Mock())
    self.assertFalse(spawn_connection.on_hit(Mock(), hit_ply, Mock(), Mock()))
