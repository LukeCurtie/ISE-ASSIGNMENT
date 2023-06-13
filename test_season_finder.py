import unittest
from season_finder import find_season


class Season_Testclass(unittest.TestCase):

  def test_summer_season(self):
    self.assertEqual(find_season('Australia', 'January'), "Summer ☀️")

  def test_autumn_season(self):
    self.assertEqual(find_season('Australia', 'April'), "Autumn 🍂")

  def test_winter_season(self):
    self.assertEqual(find_season('Australia', 'July'), "Winter ❄️")

  def test_spring_season(self):
    self.assertEqual(find_season('Australia', 'October'), "Spring 🌸")

  def test_no_season(self):
    self.assertEqual(find_season('Russia', 'June'), "Unknown")


if __name__ == '__main__':
  unittest.main()
