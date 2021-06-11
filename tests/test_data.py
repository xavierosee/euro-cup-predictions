import unittest
from euro_cup_predictions import data
import pandas as pd

fifa21_rankings = data.import_from_ea()


class TestImports(unittest.TestCase):
    def test_fifa_21_rankings(self):
        self.assertIsInstance(fifa21_rankings, pd.DataFrame)
        self.assertEqual(fifa21_rankings.shape[1], 80)
