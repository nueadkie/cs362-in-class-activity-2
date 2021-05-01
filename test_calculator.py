import unittest
import calculator

class TestCalculator(unittest.TestCase):
  def test_sum(self):
    result = calc(1,2)["sum"]
    self.assertEqual(result, 3)

  def test_diff(self):
    result = calc(5, 3)["diff"]
    self.assertEqual(result, 2)

  def test_multiple(self):
    result = calc(3, 8)["multiple"]
    self.assertEqual(result, 24)

  def test_quotient(self):
    result = calc(7, 2)["quotient"]
    self.assertEqual(result, 3.5)

  def test_div_by_zero(self):
    result = calc(2, 0)["quotient"]
    self.assertEqual(result, None)


if __name__ == '__main__':
  unittest.main()