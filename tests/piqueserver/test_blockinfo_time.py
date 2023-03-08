import unittest
from unittest.mock import MagicMock

import piqueserver.scripts.blockinfo as blockinfo

from piqueserver.player import FeatureConnection
from piqueserver.server import FeatureProtocol

from time import monotonic

class TestBlockInfoTime(unittest.TestCase):

    def test_blockinfo_on_block_removed(self):
        """Asserts that the time the block was removed is not prone to leap seconds
        by checking that it is always within a small error range from monotonic()
        """
        connection = FeatureConnection
        protocol = FeatureProtocol

        blockinfo_protocol, blockinfo_connection = blockinfo.apply_script(protocol, connection, None)

        blockinfo_connection.blocks_removed = None
        blockinfo_connection.protocol = MagicMock()
        blockinfo_connection.protocol.block_info = None

        blockinfo_connection.on_block_removed(blockinfo_connection, 1, 1, 1)
        time_of_removal = monotonic()

        assert abs(time_of_removal - blockinfo_connection.blocks_removed[0][0]) < 0.1 


    def test_blockinfo_on_kill(self):
        """Asserts that the time the kill happened is not prone to leap seconds
        by checking that it is always within a small error range from monotonic()
        """
        killer = MagicMock()
        killer.team = "Team"

        killer.teamkill_times = None

        connection = FeatureConnection
        protocol = FeatureProtocol

        blockinfo_protocol, blockinfo_connection = blockinfo.apply_script(protocol, connection, None)
        blockinfo_connection.team = "Team"
        
        blockinfo_connection.on_kill(blockinfo_connection, killer, None, None)

        time_of_kill = monotonic()

        assert abs(time_of_kill - killer.teamkill_times[0]) < 0.1