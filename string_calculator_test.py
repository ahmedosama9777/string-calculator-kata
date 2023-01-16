from unittest import TestCase

from string_calculator import StringCalculator

class TestStringCalculator(TestCase):
    def test_empty_string_return_zero(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add(""), 0)