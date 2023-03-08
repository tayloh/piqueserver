"""
test pyspades/protocol.py
"""

from twisted.trial import unittest
from pyspades import player, server, contained
from pyspades.team import Team
from unittest.mock import MagicMock, Mock
from time import monotonic

class BaseConnectionTest(unittest.TestCase):
    def test_repr(self):
        ply = player.ServerConnection(MagicMock(), MagicMock())
        repr(ply)

    def test_team_join(self):
        prot = Mock()
        prot.team_class = Team
        server.ServerProtocol._create_teams(prot)
        # Some places still use the old name
        prot.players = {}

        for team in (prot.team_1, prot.team_2, prot.team_spectator):
            ply = player.ServerConnection(prot, Mock())
            ply.spawn = Mock()
            ex_ply = contained.ExistingPlayer()
            ex_ply.team = team.id
            ply.on_new_player_recieved(ex_ply)

            self.assertEqual(ply.team, team)

    def test_respawn(self):

        ply = player.ServerConnection(MagicMock(), MagicMock())
        ply.spawn = MagicMock()
        ex_ply = contained.ExistingPlayer()
        ex_ply.team = 1
        ply.on_new_player_recieved(ex_ply)

        self.assertTrue(ply.spawn_call is None)
        ply.respawn()
        self.assertTrue(ply.spawn_call is not None)

    def test_on_block_action_recieved(self):
        ply = player.ServerConnection(MagicMock(), MagicMock())

        block_action_time = monotonic()
        ply.on_block_action_recieved(MagicMock())
        
        self.assertTrue(ply.last_block_destroy - block_action_time < 0.01)
