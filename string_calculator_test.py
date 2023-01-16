from unittest import TestCase

from string_calculator import StringCalculator

class TestStringCalculator(TestCase):
    def setUp(self) -> None:
        self.calculator = StringCalculator()

    def test_empty_string_return_zero(self):
        self.assertEqual(self.calculator.add(""), 0)
    
    def test_one_number_string(self):
        self.assertEqual(self.calculator.add("1"), 1)
    
    def test_two_numbers_separated_by_comma(self):
        self.assertEqual(self.calculator.add("1,2"), 3)
    
    def test_more_than_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)
