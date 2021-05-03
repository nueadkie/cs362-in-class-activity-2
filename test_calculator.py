import unittest
import calculator

class TestCalculator(unittest.TestCase):
  def test_sum(self):
    result = calculator.calc(1,2)["sum"]
    self.assertEqual(result, 3)

  def test_diff(self):
    result = calculator.calc(5, 3)["diff"]
    self.assertEqual(result, 2)

  def test_multiple(self):
    result = calculator.calc(3, 8)["multiple"]
    self.assertEqual(result, 24)

  def test_quotient(self):
    result = calculator.calc(7, 2)["quotient"]
    self.assertEqual(result, 3.5)

  def test_div_by_zero(self):
    result = calculator.calc(2, 0)["quotient"]
    self.assertEqual(result, None)


if __name__ == '__main__':
  unittest.main()