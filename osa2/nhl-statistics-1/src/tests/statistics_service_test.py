import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search(self):
        palaute = self.stats.search("Kurri")
        self.assertIsNotNone(palaute)
        self.assertEqual(palaute.name, "Kurri")
        self.assertEqual(palaute.team, "EDM")
        self.assertEqual(palaute.goals, 37)
        self.assertEqual(palaute.assists, 53)
    
    def test_search_empty(self):
        palaute = self.stats.search("Lorem Ipsum")
        self.assertIsNone(palaute)
    
    def test_team(self):
        palaute = self.stats.team("EDM")
        self.assertIsNotNone(palaute)
        self.assertEqual(len(palaute), 3)
    
    def test_team_empty(self):
        palaute = self.stats.search("BLU")
        self.assertIsNone(palaute)
    
    def test_top(self):
        palaute = self.stats.top(3)
        self.assertIsNotNone(palaute)
        self.assertEqual(palaute[0].name, "Gretzky")