import unittest
from temperature_comparator import compare_temperature


class Temperature_Testclass(unittest.TestCase):

  def test_temperature(self):
    self.assertEqual(compare_temperature("Mumbai", 20, 30, 25, 28, "Morning"),
                     "In appropriate temperature difference ")
    self.assertEqual(compare_temperature("Delhi", 10, 20, 15, 18, "Evening"),
                     "In appropriate temperature difference ")


if __name__ == '__main__':
  unittest.main()
