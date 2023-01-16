from unittest import TestCase

from string_calculator import StringCalculator

class TestStringCalculator(TestCase):
    def setUp(self) -> None:
        self.calculator = StringCalculator()

    def test_empty_string_return_zero(self):
        self.assertEqual(self.calculator .add(""), 0)
    
    def test_one_number_string(self):
        self.assertEqual(self.calculator .add("1"), 1)
