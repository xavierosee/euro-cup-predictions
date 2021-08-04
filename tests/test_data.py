import unittest
from euro_cup_predictions import data
import pandas as pd

fifa21_rankings = data.import_from_ea()
uefa_rankings = data.import_from_uefa()
fifacom_rankings = data.import_from_fifa()


class TestImports(unittest.TestCase):
    def test_fifa_21_rankings(self):
        self.assertIsInstance(fifa21_rankings, pd.DataFrame)
        self.assertEqual(fifa21_rankings.shape[1], 80)

    def test_uefa_rankings(self):
        self.assertIsInstance(uefa_rankings, pd.DataFrame)
        self.assertEqual(uefa_rankings.shape[1], 26)

    def test_fifa_country_rankings(self):
        self.assertIsInstance(fifacom_rankings, pd.DataFrame)
        self.assertEqual(fifacom_rankings.shape, (210, 4))
